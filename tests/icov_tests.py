from measures import icov
from tests import read_data
import numpy as np


def run_icov_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")
    ground_truth = read_data.read_array("tests/data/sim_corr.txt")

    print("\nICOV")
    R = icov.ICOV(arr, 5)
    print(R)
    print(ground_truth)
    print(R - ground_truth)
