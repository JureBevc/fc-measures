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
- ICOV
- Bayes net
- (Full correlation)
- (Patel's κ)
