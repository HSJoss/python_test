import torch as th
import copy

a = th.zeros(3, 5)
b = copy.deepcopy(a)
b[0][0] = 1

print(a)
print(b)