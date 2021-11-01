import numpy as np


def LassoShooting(X=None, y=None, lambda_=None):
    # This function computes the Least Squares parameters
    # with a penalty on the L1-norm of the parameters

    # Method used:
    #   The Shooting method of [Fu, 1998]

    # Modifications:
    #   We precompute the Hessian diagonals, since they do not
    #   change between iterations
    # [maxIter,verbose,optTol,zeroThreshold] = process_options(varargin,'maxIter',10000,'verbose',2,'optTol',1e-5,'zeroThreshold',1e-4);

    maxIter = 10000
    verbose = 0
    optTol = 1e-05
    zeroThreshold = 0.0001

    n, p = X.shape
    # Start from the Least Squares solution
    beta = np.linalg.solve((np.transpose(X) @ X + lambda_ * np.eye(p)), (np.transpose(X) @ y))

    m = 0
    XX2 = np.transpose(X) @ X * 2
    Xy2 = np.transpose(X) @ y * 2

    while m < maxIter:

        beta_old = beta
        for j in np.arange(0, p).reshape(-1):
            # Compute the Shoot and Update the variable
            S0 = sum(XX2[j, :] @ beta) - XX2[j, j] * beta[j] - Xy2[j]

            if S0 > lambda_:
                beta[j, 0] = (lambda_ - S0) / XX2[j, j]
            else:
                if S0 < - lambda_:
                    beta[j, 0] = (- lambda_ - S0) / XX2[j, j]
                else:
                    if np.abs(S0) <= lambda_:
                        beta[j, 0] = 0
        m = m + 1

        # Check termination
        if sum(np.abs(beta - beta_old)) < optTol:
            break

    if verbose:
        print('Number of iterations: %d\nTotal Shoots: %d\n' % (m, m * p))

    w = beta
    return w
