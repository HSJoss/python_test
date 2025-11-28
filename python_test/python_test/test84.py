import torch as th

x = th.rand(8, 2, 5) * 9 + 1

y = th.randint(0, 2, (8, 2, 5))

print(x)

x[y == 0] = -1e10

x = th.nn.functional.softmax(x, dim=-1)

print(y)
print(x)

z = x.size(-1)
print(z)
x2 = ((1 - 0.5) * x + th.ones_like(x).masked_fill(y == 0, 0.0) * 0.5/z)
print("DDF",x2)
x2[y == 0] = 0.0
print(x2)



z = y.sum(dim=2, keepdim=True).float()
print(z)
x2 = ((1 - 0.5) * x + th.ones_like(x).masked_fill(y == 0, 0.0) * 0.5/z)
print("DDF",x2)
x2[y == 0] = 0.0
print(x2)


# 반올림해서 출력
def pretty_print(tensor, decimals=3):
    rounded = th.round(tensor * (10 ** decimals)) / (10 ** decimals)
    print(rounded)

# 사용
pretty_print(x, decimals=3)


print("-----------------------------------")
print((1-0.5)*x)
print(th.ones_like(x)*0.5/z)
print(0.5/z)