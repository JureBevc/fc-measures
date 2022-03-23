import numpy as np
from nilearn.connectome import ConnectivityMeasure


def tangent(array_list):
    measure = ConnectivityMeasure(kind="tangent")
    matrices = measure.fit_transform(array_list)
    return matrices[0]
