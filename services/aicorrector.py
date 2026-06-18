import os
import re
import time

from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = None
if api_key:
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
        print(f"Warning: Could not initialize Gemini client: {e}")


def split_text(text: str, max_words: int = 180) -> list[str]:
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, current, current_len = [], [], 0

    for sentence in sentences:
        word_count = len(sentence.split())

        if current_len + word_count > max_words:
            chunks.append(" ".join(current))
            current, current_len = [sentence], word_count
        else:
            current.append(sentence)
            current_len += word_count

    if current:
        chunks.append(" ".join(current))

    return chunks


def ai_corrector(text: str) -> str:
    """Apply AI-based grammar correction. Falls back to original text if API unavailable."""
    if not client:
        return text
    
    chunks = split_text(text)
    results = []

    for chunk in chunks:
        prompt = f"""You are a grammar correction engine.

Correct only grammar, spelling, capitalization, and punctuation.
Do not rewrite sentences.
Do not change meaning.
Do not add or remove information.
Do not include any labels, headings, or explanations.
Return only the corrected text with no extra formatting.

Text:
{chunk}
"""
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            results.append(response.text.strip())
        except Exception as e:
            print(f"Gemini API error: {e}. Using original text.")
            results.append(chunk)

    return re.sub(r' +', ' ', " ".join(results)).strip()