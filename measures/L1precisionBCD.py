from measures.mysetdiff import mysetdiff
from measures.LassoShooting import LassoShooting
import numpy as np
from scipy.linalg import sqrtm


def L1precisionBCD(sigma_emp=None, lambda_=None):
    verbose = 1
    optTol = 1e-05
    S = sigma_emp
    p = S.shape[1-1]
    row = lambda_
    maxIter = 10
    A = np.concatenate((np.eye(p - 1, p - 1), - np.eye(p - 1, p - 1)))
    f = np.zeros((p - 1, 1))

    # Initial W
    W = S + row * np.eye(p, p)

    # Check for qp mex file
    useQP = 0
    # fprintf("useQP #d\n", useQP);
    for iter in np.arange(1, maxIter+1).reshape(-1):
        # Check Primal-Dual gap
        X = np.linalg.inv(W)
        gap = np.trace(S @ X) + row * sum(sum(np.abs(X))) - p

        # fprintf('Iter = #d, OptCond = #.5f\n',iter,gap);
        if gap < optTol:
            #fprintf('Solution Found\n');
            break
        for i in np.arange(0, p).reshape(-1):
            # Compute Needed Partitions of W and S
            s_12 = S[mysetdiff(np.arange(0, p), np.array([i])), i].reshape(-1, 1)
            # Solve with Shooting
            W_11 = W[mysetdiff(np.arange(0, p), np.array([i]))][:, mysetdiff(np.arange(0, p), np.array([i]))]
            Xsub = sqrtm(W_11)
            ysub = np.linalg.solve(Xsub, s_12)
            w = W_11 @ LassoShooting(Xsub, ysub, 2 * row)
            w = w.reshape(1, -1)[0]

            # Un-Permute
            W[mysetdiff(np.arange(0, p), np.array([i])), i] = w
            W[i, mysetdiff(np.arange(0, p), np.array([i]))] = np.transpose(w)
        # drawnow
    return X
