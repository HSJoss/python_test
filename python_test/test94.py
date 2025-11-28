import torch as th
from torch.distributions import Categorical

a = th.tensor([3, 5, 6, float("-inf")])

b = a.max(dim=-1)[0]

print(a)
print(b)


c = th.tensor([3, 5, 6, -1e10])
d = th.nn.functional.softmax(c, dim=-1)

print(c)
print(d)
e = (d > 0).sum(dim=-1, keepdim=True).float()

print(e)
print(d == 0)