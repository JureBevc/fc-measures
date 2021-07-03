import numpy as np

def entropy(c):
    norm = c / float(np.sum(c))
    norm = norm[np.nonzero(norm)]
    H = -sum(norm * np.log2(norm))  
    return H

def MI_pair(X, Y, bins):
    c_XY = np.histogram2d(X,Y,bins)[0]
    c_X = np.histogram(X,bins)[0]
    c_Y = np.histogram(Y,bins)[0]

    H_X = entropy(c_X)
    H_Y = entropy(c_Y)
    H_XY = entropy(c_XY)
    MI = H_X + H_Y - H_XY
    return MI


def mutual_information(arr, bins=5):

    n = arr.shape[0]
    MI = np.zeros((n, n))

    for ix in np.arange(n):
        for jx in np.arange(ix,n):
            MI[ix,jx] = MI_pair(arr[ix], arr[jx], bins)
            MI[jx,ix] = MI[ix,jx]
    
    return MI


