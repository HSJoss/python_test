import torch
import torch.nn.functional as F

# 예시 값
input = torch.tensor([0.0, 1.0, 2.0], requires_grad=True)
target = torch.tensor([0.0, 1.0, 2.5])

# Smooth L1 loss 계산
loss = F.smooth_l1_loss(input, target)
print(loss)