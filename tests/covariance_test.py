from measures import covariance
from tests import read_data
import numpy as np

def run_covariance_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")

    print("\nCovariance")
    R = covariance.covariance(arr)
    print(R)