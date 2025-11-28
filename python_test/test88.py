import torch as th

x = th.tensor([0.22, 0.44, 0.87, 0.775, 1.337])
y = th.tensor([1, 0, 1, 1, 0])

a = th.ones_like(x).masked_fill(y == 0, 0.0)
b = th.ones_like(x)

print(a)
print(b)
print(y)
print(y.float())
print(b[0].dtype)
print(y[0].dtype)


x2 = th.nn.functional.softmax(x, dim=-1)
print(x2)

x[y == 0] = float("-inf")
x = th.nn.functional.softmax(x, dim=-1)
print(x)

zero_indices = th.where(x == 0)
print(zero_indices[0])
zero_indices2 = (x == 0).nonzero(as_tuple=True)[0]
print(zero_indices2)

mask = (x != 0).float()
print(mask)

x[y == 0] = float("-inf")
mask = (x != float("-inf")).float()
print(mask)