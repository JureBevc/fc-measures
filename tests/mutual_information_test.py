from measures import mutual_information
from tests import read_data
import numpy as np

def run_mutual_information_test():
    d1 = read_data.read_from_file("tests/data/1.txt")
    d2 = read_data.read_from_file("tests/data/2.txt")
    d3 = read_data.read_from_file("tests/data/3.txt")
    arr = np.array([d1, d2, d3])

    print("\nMutual information")
    R = mutual_information.mutual_information(arr)
    print(R)