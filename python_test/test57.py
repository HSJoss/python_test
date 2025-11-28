import torch
import torch.nn as nn

input_shape = (3, 84, 84)

cnn = nn.Sequential(
    nn.Conv2d(in_channels=input_shape[0], out_channels=32, kernel_size=8, stride=4, padding=0),  # -> (32, 20, 20)
    nn.ReLU(),
    nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=0),  # -> (64, 9, 9)
    nn.ReLU(),
    nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=0),  # -> (64, 7, 7)
    nn.ReLU(),
    nn.Flatten()  # -> 64 * 7 * 7 = 3136
)


def _get_cnn_output_shape(input_shape):
    with torch.no_grad():
        dummy_input = torch.zeros(1, *input_shape, dtype=torch.float)
        cnn_out = cnn(dummy_input)
        flat_cnn = cnn_out.shape[1]
        return flat_cnn
    
print(_get_cnn_output_shape(input_shape))