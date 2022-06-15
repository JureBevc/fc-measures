import numpy as np
import pyinform
from nitime.algorithms.entropy import transfer_entropy as te
 
def transfer_entropy(arr, k=2):
    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(len(arr)):
        for j in range(len(arr)):
            #result[i][j] = pyinform.transferentropy.transfer_entropy(arr[i], arr[j], k=1)
            te_result, te_max = te(arr[i], arr[j], lag=k)
            result[i][j] = 1 - te_result / te_max
            #print(result[i][j])
    return result
