#import matlab.engine
import numpy as np
from measures.L1precisionBCD import L1precisionBCD


def ICOV(arr):
    cov = np.cov(arr)
    #invcov = np.linalg.inv(cov)
    invcov = np.linalg.pinv(cov)
    result = np.zeros(invcov.shape)
    for i in range(invcov.shape[0]):
        for j in range(invcov.shape[1]):
            result[i][j] = - invcov[i][j] / np.sqrt(invcov[i][i] * invcov[j][j])

    return result
