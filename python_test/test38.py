import torch as th

terminated = th.tensor([[0,0,0,1,0,0,0,0,0,0]])
mask = th.tensor([[1,1,1,1,1,1,1,1,1,1]])
mask[:, 1:] = mask[:, 1:] * (1 - terminated[:, :-1])

print(mask)