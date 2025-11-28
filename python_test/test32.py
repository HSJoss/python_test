import torch as th
a = th.tensor([[3],
              [4],
              [5]])

print(a)
print(a.shape)
print(a.unsqueeze(1).shape)
print(a.shape)
print(a[1])
print(a[0].shape)

b = a.unsqueeze(-1)
print(b)
print(b.shape)
print(b[0])
print(b[0].shape)