from measures import transfer_entropy
from tests import read_data
import numpy as np


def run_transfer_entropy_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")
    ground_truth = read_data.read_array("tests/data/sim_corr.txt")
    if np.min(arr) < 0:
        arr = arr - np.min(arr)

    print("\nTransfer entropy")
    R = transfer_entropy.transfer_entropy(arr)
    print(R)
