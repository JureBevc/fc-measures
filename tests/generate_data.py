import sys
import numpy as np

if len(sys.argv) < 2:
    exit()

N = int(sys.argv[1])

n_list = np.array([i / 10 for i in range(N)])

data1 = np.sin(n_list)
np.savetxt("data/1.txt", data1)

data2 = np.cos(n_list)
np.savetxt("data/2.txt", data2)

data3 = np.random.rand(1, N)[0] * 2 - 1
np.savetxt("data/3.txt", data3)