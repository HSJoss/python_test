import torch
epsilon = 0.5
agent_inputs = torch.randn(1, 5, 4)
print(agent_inputs[:, :, 0].shape)

random_numbers = torch.rand_like(agent_inputs[:, :, 0])
pick_random = (random_numbers < epsilon).long()
print(pick_random)

random_actions = torch.randint(0, 4, (1,)).long()  # 2번 또는 3번 액션을 선택
print(random_actions)

picked_actions = pick_random * random_actions + (1 - pick_random) * agent_inputs.max(dim=2)[1]
print(picked_actions)