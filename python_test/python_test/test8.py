import torch
input_shape = (4, 84, 84)
k = torch.zeros(1, *input_shape)
print(k.shape)