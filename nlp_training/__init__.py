import torch
from transformers import pytorch_utils
# BEGIN patch pytorch to fix device="mps" issues
def patched_isin_mps_friendly(elements, test_elements):
    if test_elements.ndim == 0:
        test_elements = test_elements.unsqueeze(0)
    return elements.tile(test_elements.shape[0], 1).eq(test_elements.unsqueeze(1)).sum(dim=0).bool().squeeze()

pytorch_utils.isin_mps_friendly = patched_isin_mps_friendly
# END pytorch to fix device="mps" issues

from . import E1_sentiment
from . import E1_sentiment
from . import E2_classification
from . import E3_textgen
from . import E4_fillmask
from . import E5_named_entities
from . import E6_answers
from . import E7_summary
from . import E8_translation

example = [
    E1_sentiment,
    E2_classification,
    E3_textgen,
    E4_fillmask,
    E5_named_entities,
    E6_answers,
    E7_summary,
    E8_translation
]

def run_example(i):
    print("running example {0}".format(i))
    if i<1 or i>len(example): raise Exception("unknown example {0}".format(i))

    res = example[i-1].run()
    print(res)