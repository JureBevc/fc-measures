import numpy as np


def full_correlation(arr):
    normed = (arr - arr.mean(axis=1)[:, np.newaxis]) / arr.std(axis=1)[:, np.newaxis]
    # print(normed.mean(axis=1))
    # print(normed.std(axis=1))

    return np.corrcoef(arr)
