import numpy as np

j = 1
d = 0
e = 0

arr = np.array([j, d, e])  # shape: (3,)
print(arr[0])
arr = np.expand_dims(arr, axis=0)
np.squeeze(arr, axis=0)
print(arr.shape)
