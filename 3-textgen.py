import common
from transformers import pipeline

common.init()

generator = pipeline("text-generation", device="mps")
res = generator([
    "In this course, we will teach you how to",
    "By default, this pipeline selects a particular"
])
print(res)