import common
from transformers import pipeline

common.init()

unmasker = pipeline("fill-mask", device="mps")
res = unmasker(
    [
        "This course will teach you all about <mask> models.",
        "By default, this pipeline selects a particular pretrained model that has been fine-tuned for <mask> in English."
    ], 
    top_k=2
)

print(res)