import torch
import torch.nn as nn
import torch.nn.functional as F

tensor = torch.randn(32, 1, 84, 84)
hidden_state = torch.randn(32, 1, 256)

input_shape = torch.randn(1, 84, 84)

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
        self.fc2 = nn.Linear(512, 256)
        self.rnn = nn.GRUCell(256, 256)
        self.fc3 = nn.Linear(256, 4)

    def _get_cnn_output_shape(self, input_shape):
        # Compute the shape of the output from CNN part by doing a dummy forward pass
        with torch.no_grad():
            n_flatten = self.cnn(torch.as_tensor(torch.zeros(1, *input_shape)).float()).shape[1]
            print(n_flatten)
        return n_flatten
    
    def init_hidden(self):
        # make hidden states on same device as model
        return self.fc2.weight.new(1, 256).zero_()

    def forward(self, inputs, hidden_state):
        # Pass input through CNN
        x = self.cnn(inputs)
        # Pass CNN output through fully connected layers
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        h_in = hidden_state.reshape(-1, 256)
        h = self.rnn(x, h_in)
        q = self.fc3(h)
        print("h", h.shape)
        print("q", q.shape)
        return q, h
    
agent = CNNAgent(input_shape.shape)
agent.forward(tensor, hidden_state)
