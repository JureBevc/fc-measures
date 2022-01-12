import sys
import numpy as np
import matlab.engine
from measures import covariance, icov, mutual_information, partial_correlation, pearson

try:
    SAMPLE_NUM = int(sys.argv[1])
except Exception as e:
    print("Invalid sample number")

print(f"Running with input sample {SAMPLE_NUM}")

# Read dataset
eng = matlab.engine.start_matlab()
content = eng.load("tests/data/HCP_rs_ts_bold1_Glasser.mat", nargout=1)

# Get sample and apply usevec
timeseries = np.array(content["data"]["bold1"]["data"]["timeseries"][SAMPLE_NUM])
usevec = np.array(content["data"]["bold1"]["data"]["usevec"][SAMPLE_NUM])[0]
usable_series = timeseries[:, usevec == 1]


print(f"Input size: {usable_series.shape}")

exit()
# Run metrics
print("\nPearson correlation")
R = pearson.pearson(usable_series)
print(R)

print("\nCovariance")
R = covariance.covariance(usable_series)
print(R)

print("\nMutual information")
R = mutual_information.mutual_information(usable_series)
print(R)

print("\nPartial correlation")
R = partial_correlation.partial_correlation(usable_series)
print(R)

print("\nICOV")
R = icov.ICOV(usable_series)
print(R)
