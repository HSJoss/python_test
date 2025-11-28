import numpy as np
import torch as th

a = th.tensor(3)
print(a)

b = np.array(3)
print(b)

values = [np.array(3), th.tensor(5).item(), 4]
#th_item = th.mean(th.stack(values)).item()
np_item = np.mean(values)

#print(th_item)
print(np_item)
print(type(np_item))

types = [type(v) for v in values]
print(types)