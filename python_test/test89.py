import torch as th
from torch.distributions import Categorical

x = th.rand(8, 2, 5) * 9 + 1
y = th.randint(0, 2, (8, 2, 5))

z = th.rand_like(x[:, :, 0])
print(x)
print(z)
print(x.shape)
print(z.shape)


pick_random = (z < 0.5).long()
print(pick_random)

random_actions = Categorical(y.float()).sample().long()
print(y)
print(random_actions)

picked_actions = pick_random * random_actions + (1 - pick_random) * x.max(dim=-1)[1]
print(picked_actions)