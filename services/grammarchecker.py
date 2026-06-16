import language_tool_python
from .aicorrector import ai_corrector
from .rules import apply_rules

tool = language_tool_python.LanguageTool("en-US", config={'maxSpellingSuggestions': 5})
tool.disabled_rules  = {'WHITESPACE_RULE', 'PUNCTUATION_PARAGRAPH_END'}
tool.enabled_rules   = {
    'SUBJECT_VERB_AGREEMENT',
    'EN_SUBJECT_VERB_AGREEMENT',
    'HE_VERB_AGR',
    'PLURAL_VERB_AFTER_THIS',
}

def check_grammar(text: str):
    text = apply_rules(text)
    matches = tool.check(text)

    SKIP_RULES = {'WHITESPACE_RULE', 'PUNCTUATION_PARAGRAPH_END'}
    matches = [m for m in matches if m.rule_id not in SKIP_RULES]

    issues = []

    for match in matches:
        start = match.offset
        end = start + match.error_length

        context = text[start:end]

        issues.append({"message": match.message, "context": context})

    lt_first = language_tool_python.utils.correct(
        text,
        matches
    )

    ai_output = ai_corrector(lt_first)

    final_matches = tool.check(
        ai_output
    )

    final_matches  = [m for m in final_matches if m.rule_id not in SKIP_RULES]

    final_corrected = language_tool_python.utils.correct(
        ai_output,
        final_matches
    )

    return {
        "original": text,
        "corrected": final_corrected,
        "issues": issues
    }