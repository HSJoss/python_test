import torch as th
from torch.distributions import Categorical

x = th.tensor([0.2, 0.5, 0.1, 0.1, 0.05, 0.05])
print(x)

y = Categorical(x).sample().long()
print(y)