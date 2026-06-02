import language_tool_python

tool = language_tool_python.LanguageTool("en-US")

def check_grammar(text: str):
    matches = tool.check(text)

    issues = []

    for match in matches:
        issues.append({"message": match.message})

    corrected_text = language_tool_python.utils.correct(text, matches)

    return {
        "original": text,
        "corrected": corrected_text,
        "issues": issues
    }