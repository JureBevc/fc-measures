#import matlab.engine
import numpy as np
from measures.L1precisionBCD import L1precisionBCD


def ICOV(arr, lamb=5):
    cov = np.cov(arr)
    input_array = cov / np.mean(np.diag(cov))

    #eng = matlab.engine.start_matlab()
    # eng.cd("ICOV-L1precision")
    #matlab_arr = matlab.double(input_array.tolist())
    #icov = eng.L1precisionBCD(matlab_arr, float(lamb / 1000))
    #icov = np.array(icov)
    #print("MATLAB ICOV:")
    # print(icov)

    icov = L1precisionBCD(input_array, float(lamb / 1000))

    return icov
