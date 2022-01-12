from measures import full_correlation
from tests import read_data
import numpy as np


def run_full_correlation_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")
    ground_truth = read_data.read_array("tests/data/sim_corr.txt")

    print("\nFull correlation")
    R = full_correlation.full_correlation(arr)
    print(R)
