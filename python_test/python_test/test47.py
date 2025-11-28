import numpy as np
import numbers

a = 3
a = np.expand_dims(a, axis=0)  # [A, ...]
print(a)
print(a.shape)

if isinstance(a, numbers.Integral):
    print("AAAA")

observation = np.eye(16)[a]

print(observation.shape)
print(observation)

b = np.array([[3],
     [4],
     [6],
     [7],
     [1]])
print(b)
print(b.shape)

observation2 = np.eye(16)[b]

print(observation2.shape)
print(observation2)


c = np.array([3,
     4,
     6,
     7,
     1])
print(c)
print(c.shape)

observation3 = np.eye(16)[c]

print(observation3.shape)
print(observation3)

