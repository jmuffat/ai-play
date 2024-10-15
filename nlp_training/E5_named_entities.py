from transformers import pipeline

def run():
    ner = pipeline("ner", grouped_entities=True, device="mps")
    return ner([
        "My name is Sylvain and I work at Hugging Face in Brooklyn.",
        "I want to go back to London, eat at The Ivy, Benihana and Din Tai Fung"
    ])
