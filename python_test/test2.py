import torch

# 예시 텐서
input_tensor = torch.tensor([[1,2,3,4,5,6]])
# 인덱스 텐서
index_tensor = torch.tensor([4].long())

# gather 사용: dim=1에서 인덱스에 해당하는 값들을 선택
result = torch.gather(input_tensor, dim=1, index=index_tensor)
print(result)