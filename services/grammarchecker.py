import language_tool_python
from .aicorrector import ai_corrector

tool = language_tool_python.LanguageTool("en-US")

def check_grammar(text: str):
    matches = tool.check(text)

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

    ai_output = ai_corrector(
        lt_first
    )

    final_matches = tool.check(
        ai_output
    )

    final_corrected = language_tool_python.utils.correct(
        ai_output,
        final_matches
    )

    return {
        "original": text,
        "corrected": final_corrected,
        "issues": issues
    }