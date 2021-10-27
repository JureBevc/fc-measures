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
- (Patel's κ) https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.25093

## Notes

### Recorded samples

Do the recorded samples have ground truth?

### Bayes net

Link to the implementation is broken

> "Tetrad IV toolbox"

https://github.com/bd2kccd/tetrad
https://www.phil.cmu.edu/tetrad/current.html

### Full correlation

The authors implemented "Full correlation" with isn't much different from the normal Pearson correlation (is it at all?). Do we still need to implement both?

> The simplest measure of pairwise similarity between two time-series is covariance. If the timeseries are normalised to unit variance this measure becomes(normalised) correlation, which we will refer to as Full correlation, to distinguish this from partial correlation.

### Patel's conditional dependence measures

Existing implementations?
Original paper too complex statistically.

[A Bayesian approach to determining connectivityof the human brain](https://onlinelibrary.wiley.com/doi/epdf/10.1002/hbm.20182)

## TODO:

- Simulacija BOLD timeseries

  - fmrisim
    > https://brainpower.readthedocs.io/en/latest/simulations.html

- Nove članki, novejše metrike (Google scholar, glej citacije originalnega članka)

  2019:

  > Application of Graph Theory for Identifying Connectivity Patterns in Human Brain Networks: A Systematic Review

  - Statistical parametric mapping (SPM)
  - Decomposition-based analysis (PCA/ICA)
  - Clustering

  > Benchmarking functional connectome-based predictive models for resting-state fMRI

  - full correlation
  - partial correlation
  - tangent space of covariance matrices (Appendix A)

- ICOV v Pythonu

- Prijava teme:
  - Metrike funkcionalne povezanosti
  - Primerjava metrik...
  - Implementacija metrik funkcionalne povezanosti


- tangent space of covariance matrices (Appendix A)