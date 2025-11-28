import torch
import torch.nn as nn
import torch.nn.functional as F


input = (4, 84, 84)

cnn = nn.Sequential(
            nn.Conv2d(4, 32, kernel_size=8, stride=4, padding=0),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=0),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.Flatten(),
        )

def _get_cnn_output_shape(input_shape):
    # Compute the shape of the output from CNN part by doing a dummy forward pass
    with torch.no_grad():
        n_flatten = cnn(torch.as_tensor(torch.zeros(1, *input_shape)).float()).shape[1]
    return n_flatten

a = _get_cnn_output_shape(input)
print(a)