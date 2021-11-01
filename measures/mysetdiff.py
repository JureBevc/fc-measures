import numpy as np


def mysetdiff(A=None, B=None):
    # MYSETDIFF Set difference of two sets of positive integers (much faster than built-in setdiff)
    # C = mysetdiff(A,B)
    # C = A \ B = { things in A that are not in B }
    if len(A) == 0:
        C = []
        return C
    else:
        if len(B) == 0:
            C = A
            return C
        else:
            bits = np.zeros(np.max([np.max(A), np.max(B)]) + 1)

            bits[A] = 1
            bits[B] = 0
            bits_args = np.argwhere(bits == 1).reshape(1, -1)[0]
            a = np.array(A)
            b = bits[A] == 1
            C = a[b]

    return C


#print(mysetdiff([1,2,3, 4], [2,3]))
