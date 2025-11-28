import torch

a = torch.tensor([[[0]],
                  [[1]],
                  [[1]],
                  [[0]]])

# 값이 1인 위치 추출
indices = torch.nonzero(a == 1, as_tuple=False)[:, 0].tolist()

# 마지막 차원이 [1]짜리일 경우 squeeze로 정리
#positions = indices[:, 0]
print(indices)  # tensor([1, 2])
