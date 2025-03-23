import torch
import torch.nn as nn
import torch.nn.functional as F

tensor = torch.randn(32, 1,84,84)
print(tensor.shape)

input_shape = torch.randn(1,84,84)

class CNNAgent(nn.Module):
    def __init__(self, input_shape):
        super(CNNAgent, self).__init__()

        # CNN Part (Based on NatureCNN)
        self.cnn = nn.Sequential(
            nn.Conv2d(input_shape[0], 32, kernel_size=8, stride=4, padding=0),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=0),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.Flatten(),
        )

        # Linear layer after CNN to extract features
        self.fc1 = nn.Linear(self._get_cnn_output_shape(input_shape), 512)
        self.fc2 = nn.Linear(512, 4)

    def _get_cnn_output_shape(self, input_shape):
        # Compute the shape of the output from CNN part by doing a dummy forward pass
        with torch.no_grad():
            n_flatten = self.cnn(torch.as_tensor(torch.zeros(1, *input_shape)).float()).shape[1]
            print(n_flatten)
        return n_flatten

    def forward(self, inputs):
        # Pass input through CNN
        x = self.cnn(inputs)
        # Pass CNN output through fully connected layers
        x = F.relu(self.fc1(x))
        q_values = self.fc2(x)
        print(q_values.shape)
        return q_values
    
agent = CNNAgent(input_shape.shape)
agent.forward(tensor)
