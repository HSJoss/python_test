obs_shape = (1, 103, 103, 3)
transpose_order = [0, 3, 1, 2]
reshape = (84, 84)  # 원하는 (H, W)

# 1단계: 순서 바꾸기
obs_shape = tuple(obs_shape[i] for i in transpose_order)  # → (1, 3, 103, 103)

# 2단계: 마지막 두 차원(H, W)을 원하는 reshape로 덮어쓰기
obs_shape = obs_shape[:2] + reshape  # → (1, 3, 84, 84)

print(obs_shape)
print(type(obs_shape))