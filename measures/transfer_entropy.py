import numpy as np
import pyinform
from nitime.algorithms import transfer_entropy as TE


def transfer_entropy(arr, k=1):
    arr = np.array(arr, dtype=int)
    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(len(arr)):
        x = arr[i]
        for j in range(len(arr)):
            y = arr[j]

            te, ce = TE(x, y, lag=k)
            result[i][j] = te / ce
            #result[i][j] = TE(x, y, lag=k)
    return result
