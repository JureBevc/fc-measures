import numpy as np
import pyinform


def transfer_entropy(arr, k=2):
    arr[arr < 0] = 0

    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            result[i][j] = pyinform.transferentropy.transfer_entropy(arr[i], arr[j], k=k)
            result[j][i] = result[i][j]
    return result
