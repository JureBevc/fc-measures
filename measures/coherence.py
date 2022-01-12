import numpy as np
import scipy


def coherence(arr, nperseg=10):

    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            _, Cxy = scipy.signal.coherence(arr[i], arr[j], nperseg=nperseg)
            result[i][j] = np.max(Cxy)
            result[j][i] = result[i][j]
    return result
