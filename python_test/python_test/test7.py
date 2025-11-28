import torch
"""avail_actions = [[1] * 11 for _ in range(5)]
print(torch.tensor(avail_actions).shape)"""

n_agents = 3
n_actions = 5

def get_avail_actions(fireflag):
    # [n_agents, n_actions] 크기의 avail_actions 텐서를 1로 초기화
    avail_actions = torch.ones(n_agents, n_actions, dtype=torch.int)

    # fireflag가 False일 경우 모든 avail_actions는 [1, 1, 1, 1]로 유지
    if not fireflag:
        return avail_actions

    # fireflag가 True일 경우, indices에 해당하는 인덱스는 0, 나머지는 1로 설정
    indices = [0, 2, 4]
      
    # indices에 해당하는 인덱스를 0으로 설정
    avail_actions[:, torch.tensor(indices)] = 0

    return avail_actions

result = get_avail_actions(True)
print(result)
print(result.shape)