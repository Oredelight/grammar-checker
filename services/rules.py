# services/rules.py

import re

COMMON_FIXES = {
    r"\bme and him was\b": "he and I were",
    r"\bher and me\b": "she and I",
    r"\bi seen\b": "I saw",
    r"\bwe was\b": "we were",
    r"\bthey was\b": "they were",
    r"\bhe do\b": "he does",
    r"\bshe dont\b": "she doesn't",
    r"\bthem are\b": "they are",
    r"\bhim and me is\b": "he and I are",
}


def apply_rules(text: str) -> str:

    fixed = text

    for pattern, replacement in COMMON_FIXES.items():

        fixed = re.sub(
            pattern,
            replacement,
            fixed,
            flags=re.IGNORECASE
        )

    return fixed