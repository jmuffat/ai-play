from transformers import pipeline

def run():
    unmasker = pipeline("fill-mask", device="mps")
    return unmasker(
        [
            "This course will teach you all about <mask> models.",
            "By default, this pipeline selects a particular pretrained model that has been fine-tuned for <mask> in English."
        ], 
        top_k=2
    )
