import torch as th

a= []
a.insert(0, 3.0)
a.insert(0, 4.0)
a.insert(0, 8.0)

a = th.tensor(a)
a = (a - a.mean()) / a.std()
print(a)