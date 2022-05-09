import numpy as np
import pandas as pd
from pingouin import partial_corr


def partial_correlation(arr, control):
    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            df = pd.DataFrame({
                "x": arr[i],
                "y": arr[j],
                "c": control
            })
            pc = partial_corr(data=df, x="x", y="y", covar="c")["r"].values[0]
            result[i][j] = pc
            result[j][i] = result[i][j]
    return result
