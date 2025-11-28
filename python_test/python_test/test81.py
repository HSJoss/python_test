import torch as th

indices = [0, 2, 4]

tensor = th.arange(1, 6).view(5, 1, 1).repeat(1, 1, 4)

print(tensor[indices])

for idx in indices:
    print(tensor[idx])