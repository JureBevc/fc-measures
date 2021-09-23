from measures import icov
from tests import read_data
import numpy as np

def run_icov_test():
    arr = read_data.read_multiple_from_file("tests/data/sim_ts.txt")
    
    print("\nICOV")
    R = icov.ICOV(arr, 5)
    print(R)