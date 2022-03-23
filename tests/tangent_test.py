from measures import tangent
from tests import read_data
import numpy as np


def run_tangent_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")

    print("\nTangent")
    arr = arr.T
    R = tangent.tangent([arr, arr, arr])
    print(R)
