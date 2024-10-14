import common
from transformers import pipeline

common.init()

classifier = pipeline("zero-shot-classification",device="mps")
res = classifier(
    [
        "This is a course about the Transformers library",
        "By default, this pipeline selects a particular pretrained model that has been fine-tuned for sentiment analysis in English. The model is downloaded and cached when you create the classifier object. If you rerun the command, the cached model will be used instead and there is no need to download the model again."
    ],
    candidate_labels=["education", "politics", "business"],
)

print(res)