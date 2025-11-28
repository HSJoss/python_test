import numpy as np
items = ['A', 'B', 'C', 'D']

# 단 1개 샘플
print(np.random.choice(items, size=1))  # ['C']  → 이게 나왔다고 'C'가 편향된 건 아님

from collections import Counter

samples = np.random.choice(items, size=1000000)
count = Counter(samples)
print(count)
