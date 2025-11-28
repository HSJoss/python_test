import torch as th
a = None
b = []
c = th.tensor([])

if a is None:
    print("Hello1")

if b is None:
    print("Hello2")

if c is None:
    print("Hello3")

if not a:
    print("Hello4")

if not b:
    print("Hello5")

"""if not c:
    print("Hello6")"""

"""if len(a)==0:
    print("Hello7")"""

if len(b)==0:
    print("Hello8")

if len(c)==0:
    print("Hello9")


import torch as th
import numpy as np

def is_empty(x):
    if x is None:
        return True
    if isinstance(x, (list, tuple, dict, set, str)):
        return len(x) == 0
    if isinstance(x, np.ndarray):
        return x.size == 0
    if isinstance(x, th.Tensor):
        return x.numel() == 0
    return False  # 기타 객체는 비어있지 않다고 판단