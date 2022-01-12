import numpy as np


def cross_correlation(arr):
    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            result[i][j] = np.max(np.correlate(arr[i], arr[j]))
            result[j][i] = result[i][j]
    return result
