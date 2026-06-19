import language_tool_python
from language_tool_python.exceptions import RateLimitError
from .aicorrector import ai_corrector
import re
from difflib import SequenceMatcher
import logging

logger = logging.getLogger(__name__)

SKIP_RULES = {'WHITESPACE_RULE', 'PUNCTUATION_PARAGRAPH_END', 'SENTENCE_WHITESPACE'}

_tool = None
_initialization_failed = False

def _get_tool():
    global _tool, _initialization_failed
    if _tool is None and not _initialization_failed:
        try:
            logger.info("Initializing LanguageTool...")
            _tool = language_tool_python.LanguageTool("en-US")
            logger.info("LanguageTool initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize LanguageTool: {e}. Will use AI corrections only.", exc_info=True)
            _initialization_failed = True
            return None
    return _tool


def check_grammar(text: str):
    tool = _get_tool()
    language_matches = []
    
    if tool is not None:
        try:
            language_matches = tool.check(text)
            logger.info(f"LanguageTool returned {len(language_matches)} matches before filtering")
            language_matches = [m for m in language_matches if m.rule_id not in SKIP_RULES]
            logger.info(f"LanguageTool returned {len(language_matches)} matches after filtering")
        except Exception as e:
            logger.error(f"LanguageTool check failed: {e}", exc_info=True)
            language_matches = []
    else:
        logger.warning("LanguageTool is not available, using AI corrections only")
    
    ai_output = ai_corrector(text)
    
    issues = []
    matched_positions = set()
    
    for match in language_matches:
        start = match.offset
        end = start + match.error_length
        context = text[start:end]
        matched_positions.add((start, end))
        issues.append({
            "message": match.message,  
            "offset": start,
            "length": match.error_length,
            "context": context
        })
    
    original_words = re.findall(r'\b\w+\b|\S', text)
    corrected_words = re.findall(r'\b\w+\b|\S', ai_output)
    
    matcher = SequenceMatcher(None, original_words, corrected_words)
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != 'equal':
            original_chunk = ' '.join(original_words[i1:i2]) if i2 > i1 else ''
            corrected_chunk = ' '.join(corrected_words[j1:j2]) if j2 > j1 else ''
            
            if original_chunk:
                pos = text.find(original_chunk)
                if pos >= 0 and (pos, pos + len(original_chunk)) not in matched_positions:
                    issues.append({
                        "message": f"'{original_chunk}' should be '{corrected_chunk}'",
                        "context": original_chunk,
                        "offset": pos,
                        "length": len(original_chunk)
                    })

    return {
        "original": text,
        "corrected": ai_output,
        "issues": issues
    }