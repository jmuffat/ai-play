from transformers import pipeline

def run():
    generator = pipeline("text-generation", device="mps")
    return generator([
        "In this course, we will teach you how to",
        "By default, this pipeline selects a particular"
    ])
