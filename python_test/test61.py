import torch as th 

l = []

a = th.randn(1, 3, 84, 84)
b = th.randn(1, 2, 84, 84)
c = 0

l.append(a)
#l.append(b)
l.append(c)
print(l)

#l = th.cat([x.reshape(1, -1) for x in l], dim=1)
l = th.cat([x for x in l], dim=1)

print(l.shape)
print(a.shape)