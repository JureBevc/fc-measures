# fc-measures

Implementation of various functional connectivity metrics

# Requirements

- Python 3.8 (required by the matlab API module)
- Python modules specified in `requirements.txt`
- `matlab` API module installed seperately and not mentioned in `requirements.txt`
- `HCP_rs_ts_bold1_Glasser.mat` file for testing purposes, inside the `tests/data` folder

## TODO

### Testing

- BOLD singla simulation

### Metrics

Basic metrics:

- ~~Pearson correlation~~
- ~~Covariance~~
- ~~Mutual information~~

Best metrics from NeuroImage paper:

- ~~Partial correlation~~
- ICOV (currently implemented in with MATLAB, rewrite to Python)
- Bayes net
- (Full correlation)
- (Patel's κ)

## Notes

The authors implemented "Full correlation" with isn't much different from the normal Pearson correlation (is it at all?). Do we still need to implement both?

> The simplest measure of pairwise similarity between two time-series is covariance. If the timeseries are normalised to unit variance this measure becomes(normalised) correlation, which we will refer to as Full correlation, to distinguish this from partial correlation.

