import torch
from transformers import pytorch_utils

# patch pytorch to fix device="mps" issues
def patched_isin_mps_friendly(elements, test_elements):
    if test_elements.ndim == 0:
        test_elements = test_elements.unsqueeze(0)
    return elements.tile(test_elements.shape[0], 1).eq(test_elements.unsqueeze(1)).sum(dim=0).bool().squeeze()

pytorch_utils.isin_mps_friendly = patched_isin_mps_friendly

# END pytorch to fix device="mps" issues

def init():
    print("init common")