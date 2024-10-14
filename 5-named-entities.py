import common
from transformers import pipeline

common.init()

ner = pipeline("ner", grouped_entities=True, device="mps")
res = ner([
    "My name is Sylvain and I work at Hugging Face in Brooklyn.",
    "I want to go back to London, eat at The Ivy, Benihana and Din Tai Fung"
])

print(res)