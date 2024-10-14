import common
from transformers import pipeline

common.init()

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en", device="mps")
res = translator([
    "Ce cours est produit par Hugging Face.",
    "Il y a mille et une manières d’envisager l’art d’escalader les montagnes."
])

print(res)

