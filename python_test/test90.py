import torch as th

a = th.tensor([0.5, 0.7, 0, 0.1])

a[2] = float("-inf")

print(a)

a = th.nn.functional.softmax(a, dim=-1)

print(a)

n = (a > 0).sum(dim=-1, keepdim=True).float()

print(n)

b = th.ones_like(a).masked_fill(a == 0, 0.0)

print(b)