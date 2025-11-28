import torch

rewards = torch.randn(32, 1000, 3)

for i in range(rewards.shape[1]):  # 1000번 반복
    # [32, 1] 형태로 보상 값 가져오기
    reward_at_step = rewards[:, i, :]  # (배치 크기, 1) 형태로 가져오기
    print(f"Step {i}, Rewards: {reward_at_step.shape}")
    print(reward_at_step)