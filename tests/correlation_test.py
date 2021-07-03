from measures import pearson, covariance
from tests import read_data
import numpy as np

d1 = read_data.read_from_file("tests/data/1.txt")
d2 = read_data.read_from_file("tests/data/2.txt")
d3 = read_data.read_from_file("tests/data/3.txt")
arr = np.array([d1, d2, d3])

print("\nPearson correlation")
R = pearson.pearson(arr)
print(R)

print("\nCovariance")
R = covariance.covariance(arr)
print(R)