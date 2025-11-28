import torch as th

x = th.tensor([5.0, 0.5, -2.0])
print(x)

x = th.nn.functional.softmax(x, dim=-1)
# 반올림해서 출력
def pretty_print(tensor, decimals=3):
    rounded = th.round(tensor * (10 ** decimals)) / (10 ** decimals)
    print(rounded)

x2 = ((1 - 0.01) * x + th.ones_like(x) * 0.01/th.tensor([2]))


# 사용
pretty_print(x, decimals=3)

pretty_print(x2, decimals=3)