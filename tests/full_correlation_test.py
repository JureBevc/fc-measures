from measures import full_correlation
from tests import read_data
import numpy as np


def run_full_correlation_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")

    print("Full correlation")
    R = full_correlation.full_correlation(arr)
    print(R)
