from measures import pearson
from tests import read_data
import numpy as np

def run_correlation_test():
    d1 = read_data.read_from_file("tests/data/1.txt")
    d2 = read_data.read_from_file("tests/data/2.txt")
    d3 = read_data.read_from_file("tests/data/3.txt")
    arr = np.array([d1, d2, d3])

    print("\nPearson correlation")
    R = pearson.pearson(arr)
    print(R)