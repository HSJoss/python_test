import numpy as np

# 3행 5열의 랜덤 값 배열 생성
np_array = np.random.rand(3, 1)  # 값은 [0.0, 1.0) 사이의 실수
print(np_array[:, :1].shape)


import torch

# 3행 5열의 랜덤 값 텐서 생성
torch_tensor = torch.rand(3, 1)  # 값은 [0.0, 1.0) 사이의 실수
print(torch_tensor[:, :1].shape)
