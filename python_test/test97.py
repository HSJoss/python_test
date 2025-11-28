import torch
import torch.nn as nn


class SharedGroupedMLP(nn.Module):
    def __init__(self, pair_dim=2, hidden_dim=8, output_dim=1):
        super().__init__()
        self.shared_mlp = nn.Sequential(
            nn.Linear(pair_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
    
    def forward(self, q_vec, a_vec):
        # (batch_size, n, 2)
        pairs = torch.stack([q_vec, a_vec], dim=2)
        # reshape to (batch_size * n, 2)
        pairs_flat = pairs.view(-1, 2)
        z_flat = self.shared_mlp(pairs_flat)
        z_flat = z_flat.squeeze(-1)
        # reshape back to (batch_size, n)
        z = z_flat.view(q_vec.shape[0], q_vec.shape[1])
        return z
    

model = SharedGroupedMLP()

q = torch.tensor([[1.0, 10.0]])
a = torch.tensor([[2.0, 20.0]])

out1 = model(q, a)
print(out1)

# q 바꿔보기 (q[0,0]만 바꾼다)
q2 = torch.tensor([[9.0, 10.0]])
out2 = model(q2, a)
print(out2)

# a 바꿔보기 (a[0,1]만 바꾼다)
a3 = torch.tensor([[2.0, 99.0]])
out3 = model(q, a3)
print(out3)