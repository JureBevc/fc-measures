from measures import mutual_information
from tests import read_data
import numpy as np


def run_mutual_information_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")
    ground_truth = read_data.read_array("tests/data/sim_corr.txt")

    print("\nMutual information")
    R = mutual_information.mutual_information(arr)
    print(R)
    print(ground_truth)
    print(R - ground_truth)
