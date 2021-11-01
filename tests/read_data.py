import pandas as pd
import numpy as np


def read_from_file(file_name):
    df = pd.read_csv(file_name, sep=",", header=None)
    return df.values.reshape((1, -1))[0]


def read_multiple_from_file(file_name):
    df = pd.read_csv(file_name, sep=",", header=None)
    return np.transpose(df.values)


def read_array(file_name):
    df = pd.read_csv(file_name, sep=",", header=None)
    return df.values
