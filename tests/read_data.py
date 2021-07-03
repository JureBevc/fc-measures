import pandas as pd
import numpy as np

def read_from_file(file_name):
    df = pd.read_csv(file_name, sep=",")
    return df.values.reshape((1, -1))[0]