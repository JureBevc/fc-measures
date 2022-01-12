from measures import tangent
from tests import read_data
import numpy as np


def run_tangent_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")
    ground_truth = read_data.read_array("tests/data/sim_corr.txt")

    print("\nTangent")
    R = tangent.tangent(arr)
    print(R)
