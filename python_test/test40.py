import numpy as np

a = np.array([1, 2, 3])                 # 1차원
b = np.array([[[1], [2]], [[3], [4]]])  # 3차원

print(a.ndim)  # 출력: 1
print(b.ndim)  # 출력: 3

print(a.shape)
print(b.shape)

print(len(a.shape))
print(len(b.shape))