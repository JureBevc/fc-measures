import matlab.engine
import numpy as np


def L1precisionBCD():
    pass

def ICOV(arr, lamb=5):
    eng = matlab.engine.start_matlab()
    eng.cd("ICOV-L1precision")


    #icov=L1precisionBCD(cov/mean(diag(cov)), lamb/1000)
    cov = np.cov(arr)
    input_array = cov / np.mean(np.diag(cov))

    matlab_arr = matlab.double(input_array.tolist())
    icov = eng.L1precisionBCD(matlab_arr, float(lamb / 1000))
    icov = np.array(icov)
    
    return icov
