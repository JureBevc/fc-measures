import numpy as np
from nitime.algorithms import conditional_entropy, entropy


def nitime_transform_entropy_with_extra_return_value(x, y, lag=1):
    # Future of i
    Fi = np.roll(x, -lag)
    # Past of i
    Pi = x
    # Past of j
    Pj = y

    # Transfer entropy
    Inf_from_Pi_to_Fi = conditional_entropy(Fi, Pi)

    # Same as cond_entropy(Fi, Pi_Pj)
    H_y = entropy(Pi, Pj)
    H_yx = entropy(Fi, Pj, Pi)
    Inf_from_Pi_Pj_to_Fi = H_yx - H_y

    TE_from_j_to_i = Inf_from_Pi_to_Fi - Inf_from_Pi_Pj_to_Fi

    return TE_from_j_to_i, Inf_from_Pi_to_Fi

def transfer_entropy(arr, k=1):
    arr = np.array(arr, dtype=int)
    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(len(arr)):
        x = arr[i]
        for j in range(len(arr)):
            y = arr[j]

            te, ce = nitime_transform_entropy_with_extra_return_value(x, y, lag=k)
            result[i][j] = te / ce
            #result[i][j] = TE(x, y, lag=k)
    return result
