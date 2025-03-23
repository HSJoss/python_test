import torch
import torch.nn.functional as F

# 예시 예측값과 목표값
input = torch.tensor([0.5, 2.0, 3.0])
target = torch.tensor([0.0, 2.0, 3.5])

# Smooth L1 Loss 계산
loss = F.smooth_l1_loss(input, target)

print(f'Smooth L1 Loss: {loss.item()}')