import numpy as np


def partial_correlation(arr):
    """
    Explanation:
    https://stats.stackexchange.com/questions/140080/why-does-inversion-of-a-covariance-matrix-yield-partial-correlations-between-ran
    """
    try:
        PR = -np.linalg.inv(np.corrcoef(arr))
        np.fill_diagonal(PR, 1)
        return PR
    except np.linalg.LinAlgError:
        # Attempt pseudo-inverse
        PR = -np.linalg.pinv(np.corrcoef(arr))
        np.fill_diagonal(PR, 1)
        return PR
