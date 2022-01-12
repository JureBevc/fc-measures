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
- ~~ICOV~~
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

  - neurolib:

    > https://www.biorxiv.org/content/10.1101/2021.02.18.431886v1.abstract

    > https://github.com/neurolib-dev/neurolib

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

- tangent space of covariance matrices (Appendix A)

# Meeting notes

- ICOV je zdaj v celoti v Pythonu

  > https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006196

  - majhna razlika zaradi računanja inverza matrik (4 decimalna mesta)

  > https://www.nature.com/articles/s41598-020-57915-w

- Nilearn

  > https://nilearn.github.io/stable/index.html

- Vizualizacija signala

- Generator BOLD signala

# Meeting notes

- Neurolib: Nova knjižnica za Python, ima na voljo matriko funkcijske konektivnosti. Je to dovolj za ground truth?
- Signal resnica + noise, robustnost na noise, evalvacija na oboje
- Vizualizacija signala: Katere stvari bi bilo smiselno prikazati? Signal, korelacije, vizualizacija grafa/konektoma?

https://d26ua9paks4zq.cloudfront.net/cb/3d/5d5676cd48bc86d0b3c3c10ffd3a/image-getty-98326931.jpg

https://www.fieldtriptoolbox.org/assets/img/workshop/madrid2019/tutorial_erp/tsk_databrowser.png

- TODO: Ostale metrike
