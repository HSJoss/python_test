import numpy as np

# def pad_observation(obs, visible=7):
#     """
#     obs: np.ndarray of shape (2, nrow, ncol)
#     visible: int, must be odd (e.g., 3, 5, 7...)
#     returns: np.ndarray of shape (2, nrow + 2*pad, ncol + 2*pad)
#     """
#     assert visible % 2 == 1, "visible 값은 홀수여야 합니다."
#     pad = (visible - 1) // 2

#     # 패딩 값 설정
#     pad_values = [0, -1]  # 채널 0은 0으로, 채널 1은 -1로

#     padded_obs = np.stack([
#         np.pad(
#             obs[chan],
#             pad_width=pad,
#             mode="constant",
#             constant_values=pad_val
#         )
#         for chan, pad_val in enumerate(pad_values)
#     ])

#     return padded_obs

def pad_observation(obs, visible=7):
    """
    obs: np.ndarray of shape (2, H, W)
    visible: odd int (e.g., 3, 5, 7), determines how much padding to apply
    returns: padded obs of shape (2, H + 2*pad, W + 2*pad)
    """
    assert visible % 2 == 1, "visible must be an odd number"
    pad = (visible - 1) // 2

    pad_values = [0, -1]  # 채널 0은 0 패딩, 채널 1은 -1 패딩

    padded_obs = np.stack([
        np.pad(
            obs[c], 
            pad_width=((pad, pad), (pad, pad)), 
            mode="constant", 
            constant_values=pad_values[c]
        )
        for c in range(obs.shape[0])
    ])

    return padded_obs

def crop_centered_observation(padded_obs, visible=7):
    """
    padded_obs: np.ndarray, shape (2, H + 2*pad, W + 2*pad)
    visible: int, odd, crop size (e.g., 3, 5, 7)
    
    Returns: cropped_obs of shape (2, visible, visible)
    with the agent at the center.
    """
    assert visible % 2 == 1, "visible must be an odd number"

    agent_pos = np.argwhere(padded_obs[0] == 1)
    assert agent_pos.shape[0] == 1, "Agent must have a unique position in channel 0"
    agent_y, agent_x = agent_pos[0]

    half = visible // 2

    # Crop 주변에서 visible x visible 잘라내기
    cropped_obs = padded_obs[
        :,
        agent_y - half : agent_y + half + 1,
        agent_x - half : agent_x + half + 1
    ]

    return cropped_obs

obs = np.zeros((2, 4, 4), dtype=np.int32)
obs[0, 1, 2] = 1  # agent 위치

padded = pad_observation(obs)
print(padded.shape)  # (2, 10, 10)
print(padded[0])     # 채널 0 확인
print(padded[1])     # 채널 1 (-1로 패딩)

cropped = crop_centered_observation(padded)

print(cropped.shape)  # (2, 7, 7)
print(cropped[0])     # 채널 0 확인
print(cropped[1])     # 채널 1 (-1로 패딩)