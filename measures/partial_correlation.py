from re import template
import numpy as np
import pandas as pd
from pingouin import partial_corr


def partial_correlation(arr, control):

    template_df = pd.DataFrame()
    for i in range(len(control)):
        template_df[f"c{i}"] = control[i]
    control_columns = template_df.columns

    result = np.zeros((arr.shape[0], arr.shape[0]))
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            df = template_df
            df["x"] = arr[i]
            df["y"] = arr[j]
            pc = partial_corr(data=df, x="x", y="y", covar=control_columns)["r"].values[0]
            result[i][j] = pc
            result[j][i] = result[i][j]
    return result
