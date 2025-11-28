import numpy as np
import matplotlib.pyplot as plt

samples = np.random.uniform(0.6, 0.8, size=100)

plt.hist(samples, bins=30, color='skyblue', edgecolor='black')
plt.title('Uniform Distribution Samples (0.6 to 0.8)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()




import random
from collections import Counter

n = 10
trials = 1_000_000
counts = Counter()

for _ in range(trials):
    x = random.randrange(n)
    counts[x] += 1

for i in range(n):
    print(f"{i}: {counts[i]} ({counts[i]/trials:.4%})")
