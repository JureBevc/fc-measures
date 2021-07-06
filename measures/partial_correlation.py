import numpy as np


def partial_correlation(arr):
    PR = -np.linalg.inv(np.corrcoef(arr))
    np.fill_diagonal(PR, 1)
    return PR
