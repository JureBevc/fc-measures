import os
import numpy as np
from brainiak.utils import fmrisim
from brainiak.utils.fmrisim_real_time_generator import generate_data
import matplotlib.pyplot as plt

"""
# Inputs for generate_signal
dimensions = np.array([10, 10, 10])  # What is the size of the brain
feature_size = [5]
feature_type = ['cube']
feature_coordinates = np.array([[4, 4, 4]])
signal_magnitude = [30]

# Generate a volume representing the location and quality of the signal
volume = fmrisim.generate_signal(dimensions=dimensions,
                                 feature_coordinates=feature_coordinates,
                                 feature_type=feature_type,
                                 feature_size=feature_size,
                                 signal_magnitude=signal_magnitude,
                                 )

# Mask the volume to be the same shape as a brain
mask, _ = fmrisim.mask_brain(dimensions, mask_self=None,)
brain = volume * mask
print(brain)
"""

data_dir = "simulated"

#generate_data(data_dir, {})


def get_data(file_name):
    data_file = os.path.join(data_dir, file_name)
    return np.load(data_file)


mask_file = os.path.join(data_dir, "mask.npy")
mask = np.load(mask_file)

data = get_data("rt_100.npy")

n = 30
tmp = data[n]
m = mask[n] == 0
tmp[m] = 0
print(tmp.shape)

plt.matshow(tmp)
plt.savefig("test.png")
