import numpy as np
from nilearn.connectome import ConnectivityMeasure


def tangent(arr):
    measure = ConnectivityMeasure(kind="correlation")
    input_arr = arr.T
    matrices = measure.fit_transform([input_arr])
    return matrices[0]
