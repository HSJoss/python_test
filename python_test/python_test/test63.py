import copy

a = {"obs": 3, "state":5}

def f(a):
    a = copy.deepcopy(a)
    a["s"] = 7

print(a)

f(a)

print(a)