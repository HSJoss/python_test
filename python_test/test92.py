import torch
import torch.nn as nn

bn = nn.BatchNorm1d(10)

for name, buf in bn.named_buffers():
    print(name, buf.shape, buf.requires_grad)