import numpy as np
from sklearn.metrics.cluster import normalized_mutual_info_score


def mutual_information(arr, bins=5):

    n = arr.shape[0]
    MI = np.zeros((n, n))

    for ix in np.arange(n):
        for jx in np.arange(ix, n):
            MI[ix, jx] = normalized_mutual_info_score(arr[ix], arr[jx])
            MI[jx, ix] = MI[ix, jx]

    return MI
