import torch
import torch.nn as nn

# 간단한 선형 신경망 정의
model = nn.Linear(9, 2)  # 입력 크기 4, 출력 크기 2

# int64 타입 입력
inputs = []
input_tensor = torch.tensor([[1, 2, 3, 4]], dtype=torch.int64)
input_tensor2 = torch.tensor([[5, 6, 7, 8, 9]], dtype=torch.float32)
inputs.append(input_tensor)
inputs.append(input_tensor2)

input = torch.cat(inputs, dim=1)
print(input)
print(input.shape)
print(input.dtype)

# 모델 출력 시도
try:
    output = model(input)
    print("출력:", output)
except Exception as e:
    print("에러 발생:", e)