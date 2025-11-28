import torch as th

filled = th.tensor([
    [1, 1, 0, 0],  # sum=3
    [1, 0, 0, 0],  # sum=1
    [1, 1, 0, 1],  # sum=4 ← max
])

a = th.sum(filled, 1).max(0)[0]

print(a)