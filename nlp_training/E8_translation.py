from transformers import pipeline

def run():
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en", device="mps")
    return translator([
        "Ce cours est produit par Hugging Face.",
        "Il y a mille et une manières d’envisager l’art d’escalader les montagnes."
    ])



