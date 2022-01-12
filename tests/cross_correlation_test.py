from measures import cross_correlation
from tests import read_data
import numpy as np


def run_cross_correlation_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")
    ground_truth = read_data.read_array("tests/data/sim_corr.txt")

    print("\nCross correlation")
    R = cross_correlation.cross_correlation(arr)
    print(R)
