import numpy as np

# 주어진 값
epsilon_max = 1.0
epsilon_min = 0.05
decay_rate = 0.001

# 최소값에 도달하는 t를 계산
t_min = -np.log((epsilon_min - epsilon_max) / (epsilon_min)) / decay_rate
print(t_min)