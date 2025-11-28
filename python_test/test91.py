import torch as th

a = (2, 3, 3, 5, 2, 4)

b = th.rand(2, 3, 15, 8)

c = b.reshape(-1, a[2]*a[3], *a[4:])

print(c.shape)