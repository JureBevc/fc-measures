import sys
import matplotlib.pyplot as plt
import read_data

if len(sys.argv) < 2:
    exit()

for i in range(1, len(sys.argv)):
    file_name = sys.argv[i]
    arr = read_data.read_from_file(file_name)
    plt.plot(arr)

plt.show()