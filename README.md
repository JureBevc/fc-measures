# fc-measures

Implementation of various functional connectivity metrics

# Requirements

- Python 3.8 (required by the matlab API module)
- Python modules specified in `requirements.txt`

# Description

Metrics are implemented inside `measures`. The tested metrics are in:

```
pearson.py
icov.py
corss_correlation.py
mutual_information.py
transfer_entropy.py
coherence.py
```

# Tests

The available test are:

```
shift_test.py
noise_test.py
structure_test.py
```
