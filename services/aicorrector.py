import os
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

MODEL_NAME = "grammarly/coedit-large"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(device)

def chunk_text(text, chunk_size=400):
    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(
            " ".join(words[i:i + chunk_size])
        )

    return chunks

def ai_corrector(text: str):

    chunks = chunk_text(text, chunk_size=200)

    corrected_chunks = []

    for chunk in chunks:

        prompt = f"Fix grammatical errors in this sentence: {chunk}"
        
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
                early_stopping=True,
                repetition_penalty=1.3
            )

        corrected = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        corrected_chunks.append(corrected)

    return " ".join(corrected_chunks)