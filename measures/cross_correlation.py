import numpy as np


def cross_correlation(arr):
    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(len(arr)):
        x = (arr[i] - np.mean(arr[i])) / (np.std(arr[i]) * len(arr[i]))
        for j in range(i, len(arr)):
            y = (arr[j] - np.mean(arr[j])) / (np.std(arr[j]))
            result[i][j] = np.max(np.correlate(x, y, mode="same"))
            result[j][i] = result[i][j]
    return result
