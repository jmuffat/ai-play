from transformers import pipeline

def run():
    question_answerer = pipeline("question-answering", device="mps")
    return [
        question_answerer(
            question="Where do I work?",
            context="My name is Sylvain and I work at Hugging Face in Brooklyn",
        ),
        question_answerer(
            question="When is the model loaded?",
            context="By default, this pipeline selects a particular pretrained model that has been fine-tuned for sentiment analysis in English. The model is downloaded and cached when you create the classifier object. If you rerun the command, the cached model will be used instead and there is no need to download the model again.",
        )
    ] 
