from datetime import time
from tests import correlation_test, covariance_test, mutual_information_test, partial_correlation_test
from tests import icov_tests

import matlab.engine
import numpy as np

#eng = matlab.engine.start_matlab()
#content = eng.load("tests/data/HCP_rs_ts_bold1_Glasser.mat", nargout=1)
# print(content["data"]["bold1"]["data"].keys())

#timeseries = np.array(content["data"]["bold1"]["data"]["timeseries"])
#usevec = np.array(content["data"]["bold1"]["data"]["usevec"])
# print(timeseries.shape)
# exit()

correlation_test.run_correlation_test()
covariance_test.run_covariance_test()
mutual_information_test.run_mutual_information_test()
partial_correlation_test.run_partial_correlation_test()
icov_tests.run_icov_test()
