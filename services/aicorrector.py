import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re

MODEL_NAME = "grammarly/coedit-large"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(device)

model.eval()

def split_text(text, max_words=180):

    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current = []

    current_len = 0

    for sentence in sentences:
        word_count = len(sentence.split())

        if current_len + word_count > max_words:
            chunks.append(" ".join(current))
            current = [sentence]
            current_len = word_count
        else:
            current.append(sentence)
            current_len += word_count

    if current:
        chunks.append(" ".join(current))

    return chunks

def ai_corrector(text: str):

    chunks = split_text(text)

    results = []

    for chunk in chunks:

        prompt = f"Correct grammar without changing meaning: {chunk}"

        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to(device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=128,
                num_beams=1,
                do_sample=False
            )

        corrected = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        results.append(corrected)

    return " ".join(results)