from scipy.stats import truncnorm
import numpy as np
import matplotlib.pyplot as plt

# 설정
mean = 0.7
std = 0.05
lower, upper = 0.6, 0.8

# truncnorm 파라미터 변환 (정규분포 기준)
a, b = (lower - mean) / std, (upper - mean) / std

# 샘플 생성
samples = truncnorm.rvs(a, b, loc=mean, scale=std, size=10000)

# 시각화
plt.hist(samples, bins=50, density=True, color='skyblue', edgecolor='black')
plt.title("Truncated Normal Distribution (0.6 ~ 0.8)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()

# 평균 확인
print(f"Sample mean: {np.mean(samples):.4f}")
