import numpy as np

obs = 3

n_states = 16

# One-hot encoding
obs_one_hot = np.eye(n_states)[obs]
print(obs)          # 예: 3
print(obs_one_hot)  # 예: [0. 0. 0. 1. 0. ... 0.]
print(obs_one_hot.shape)