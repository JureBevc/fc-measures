from measures import partial_correlation
from tests import read_data
import numpy as np


def run_partial_correlation_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")
    ground_truth = read_data.read_array("tests/data/sim_corr.txt")

    print("\nPartial correlation")
    R = partial_correlation.partial_correlation(arr)
    print(R)