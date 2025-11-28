import torch as th
a = th.rand(3, 1)

print(a.shape)
print(a)
print(a[:, :-1].shape)
print(a[:, :-1])