import numpy as np

# 배열 생성
arr = np.zeros((2, 4, 4), dtype=int)

# 첫 번째 채널에서 하나만 1로 설정
arr[0, 1, 2] = 1  # 예: (채널 0, 행 1, 열 2)
arr[1, :, :] = 3

pos = np.argwhere(arr[0] == 2)
if pos.size == 0:
    raise ValueError(f"Agent 위치를 찾을 수 없습니다.")
row, col = pos[0]

print(arr)

print(pos)
print(row, col)
