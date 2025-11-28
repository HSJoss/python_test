import numpy as np

def bounded_poisson(lam, size, max_val):
    samples = []
    while len(samples) < size:
        s = np.random.poisson(lam)
        if s <= max_val:
            samples.append(s)
    return np.array(samples)


import math

def poisson_pmf(k, lam):
    return (lam ** k) * math.exp(-lam) / math.factorial(k)

# 예시: λ = 4일 때, k = 0부터 10까지 확률 계산
lam = 8
for k in range(30):
    prob = poisson_pmf(k, lam)
    print(f"P(X = {k}) = {prob:.5f}")