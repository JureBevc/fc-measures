from measures import pearson
from tests import read_data
import numpy as np

def run_correlation_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")
    
    print("\nPearson correlation")
    R = pearson.pearson(arr)
    print(R)