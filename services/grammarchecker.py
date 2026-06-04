import language_tool_python
from .aicorrector import ai_corrector

tool = language_tool_python.LanguageTool("en-US", config={'maxSpellingSuggestions': 5})
tool.enabled_rules = {'PASSIVE_VOICE', 'OXFORD_SPELLING_ADJECTIVES'}

def check_grammar(text: str):
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

    ai_output = ai_corrector(f"Fix grammar: {lt_first}")

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