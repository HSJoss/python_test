import numpy as np
import matplotlib.pyplot as plt

alpha = 7
beta = 3

samples = np.random.beta(alpha, beta, size=10000)

plt.hist(samples, bins=50, density=True)
plt.title(f"Beta Distribution (α={alpha}, β={beta})")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()

print(f"Sample mean: {np.mean(samples):.4f}")