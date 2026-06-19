from .aicorrector import ai_corrector
import re
from difflib import SequenceMatcher
import logging

logger = logging.getLogger(__name__)


def check_grammar(text: str):
    ai_output = ai_corrector(text)
    
    issues = []
    original_words = re.findall(r'\b\w+\b|\S', text)
    corrected_words = re.findall(r'\b\w+\b|\S', ai_output)
    
    matcher = SequenceMatcher(None, original_words, corrected_words)
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != 'equal':
            original_chunk = ' '.join(original_words[i1:i2]) if i2 > i1 else ''
            corrected_chunk = ' '.join(corrected_words[j1:j2]) if j2 > j1 else ''
            
            if original_chunk:
                pos = text.find(original_chunk)
                if pos >= 0:
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