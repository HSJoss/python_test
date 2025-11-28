import torch as th

vshape = (1,5)

a = th.zeros(10*2, *vshape)

print(a.shape)