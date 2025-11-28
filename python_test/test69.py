import torch

q_values = torch.tensor([
    [1.0, 2.0, 3.0],
    [0.5, 0.2, 0.9]
])  # shape: (2, 3)

actions_long = torch.tensor([2, 0], dtype=torch.long)
actions_int = torch.tensor([2, 0], dtype=torch.int)  # torch.int == torch.int32

# ✅ OK: long
q_values.gather(1, actions_long.unsqueeze(1))
# tensor([[3.0000], [0.5000]])

# ❌ 에러: int (int32)
q_values.gather(1, actions_int.unsqueeze(1))
# RuntimeError: Index tensor must be long or byte
