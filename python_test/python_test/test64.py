import numpy as np

def create_input_tensor(map_data, position):
    x, y = position
    map_array = np.array(map_data)
    
    # 채널 0: 위치만 1, 나머지 0
    pos_channel = np.zeros_like(map_array)
    pos_channel[x][y] = 1  # 주의: (x, y)인데 numpy는 [row][col] -> [y][x]

    # 채널 1: map 자체
    map_channel = map_array

    # 채널을 쌓아서 (2, H, W) 형태로 만들기
    input_tensor = np.stack([pos_channel, map_channel], axis=0)

    return input_tensor


import numpy as np

def pad_with_weighted_summary(full_map, cropped_map):
    agent_channel = full_map[0]
    map_channel = full_map[1]
    
    # Step 1: 에이전트 위치 찾기
    agent_pos = np.argwhere(agent_channel == 1)
    if len(agent_pos) == 0:
        raise ValueError("Agent not found.")
    ax, ay = agent_pos[0]

    z = cropped_map.shape[1]  # cropped_map size (z, z)
    crop_radius = z // 2

    # Step 2: crop 영역의 실제 full_map 좌표 계산
    top = ax - crop_radius
    left = ay - crop_radius
    bottom = ax + crop_radius + 1
    right = ay + crop_radius + 1

    # Step 3: 새 맵 크기 정의
    padded_size = z + 2
    padded_map = np.zeros((1, padded_size, padded_size), dtype=np.float32)

    # Step 4: 중앙 crop 삽입
    padded_map[0, 1:-1, 1:-1] = cropped_map[0]

    # Step 5: 외곽 영역에 대해 요약값 계산
    def weighted_summary_line(values):
        result = 0
        count = 0
        weight = 0.9
        for v in values:
            if v != 0:
                result += (weight * v)
                count += 1
            weight *= 0.9
        return result / count if count > 0 else 0.0

    H, W = map_channel.shape

    # 위쪽 행
    for i in range(z):
        col = left + i
        if 0 <= col < W:
            values = [map_channel[r, col] for r in range(top - 1, -1, -1)]
            padded_map[0, 0, i + 1] = weighted_summary_line(values)

    # 아래쪽 행
    for i in range(z):
        col = left + i
        if 0 <= col < W:
            values = [map_channel[r, col] for r in range(bottom, H)]
            padded_map[0, -1, i + 1] = weighted_summary_line(values)

    # 왼쪽 열
    for i in range(z):
        row = top + i
        if 0 <= row < H:
            values = [map_channel[row, c] for c in range(left - 1, -1, -1)]
            padded_map[0, i + 1, 0] = weighted_summary_line(values)

    # 오른쪽 열
    for i in range(z):
        row = top + i
        if 0 <= row < H:
            values = [map_channel[row, c] for c in range(right, W)]
            padded_map[0, i + 1, -1] = weighted_summary_line(values)

    #return padded_map
    return np.round(padded_map, 2)



def pad_observation(obs, visible=7):
    """
    obs: np.ndarray of shape (2, H, W)
    visible (int): Must be odd (e.g., 3, 5, 7). Determines padding size.
    return: padded obs of shape (2, H + 2*pad, W + 2*pad)
    """
    assert visible % 2 == 1, "visible must be an odd number."
    pad = (visible - 1) // 2

    # Define padding values for each channel
    # Channel 0 (agent position): pad with 0 (no agent)
    # Channel 1 (map values): pad with 4 to represent 'outside' or invalid region
    pad_values = [0, 0]

    padded_obs = np.stack([
        np.pad(
            obs[chan],
            pad_width=pad,
            mode="constant",
            constant_values=np.uint8(pad_val)
        )
        for chan, pad_val in enumerate(pad_values)
    ])
    return padded_obs

def crop_observation(padded_obs, visible=7):
    """
    padded_obs: np.ndarray of shape (2, H + 2*pad, W + 2*pad)
    visible (int): Must be odd (e.g., 3, 5, 7). Determines crop size.
    return: cropped obs of shape (1, visible, visible) with the agent at the center.
    """
    assert visible % 2 == 1, "visible must be an odd number"

    # Extract the agent position from channel 0
    agent_pos = np.argwhere(padded_obs[0] == 1)
    assert agent_pos.shape[0] == 1, "Agent must have a unique position in channel 0"
    if agent_pos.size == 0:
        raise ValueError("Agent position not found in observation.")
    agent_y, agent_x = agent_pos[0]

    half = visible // 2

    # Crop a (visible x visible) region centered on the agent
    crop_obs = padded_obs[
        :,
        agent_y - half : agent_y + half + 1,
        agent_x - half : agent_x + half + 1
    ]
    #return crop_obs
    return crop_obs[1:2]  # Return only the map info channel (channel 1)



# 예시 사용
map = [
    [2,2,2,2,1,2,2,2],
    [2,2,2,2,2,2,1,2],
    [2,2,2,1,2,2,2,2],
    [2,2,2,2,2,1,2,1],
    [2,2,2,1,2,2,2,1],
    [2,1,1,2,2,2,1,2],
    [2,1,2,2,1,2,1,2],
    [2,2,2,1,2,2,2,3],
]

position = (1, 2)
#position = (6, 5)  # (x, y)
map2 = create_input_tensor(map, position)

full_map = pad_observation(map2)

cropped_map = crop_observation(full_map)

print(full_map.shape)

print(cropped_map.shape)

print(full_map)

print(cropped_map)

expanded = pad_with_weighted_summary(full_map, cropped_map)

print(expanded)
print(expanded.shape)
#print(np.round(expanded, 2))