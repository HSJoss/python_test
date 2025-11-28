import torch
import torch.nn.functional as F

# 랜덤 텐서 생성
logits = torch.randn(1, 4)
print("Logits:", logits)

# 마스크 생성 (0 또는 1로 이루어진)
mask = torch.randint(0, 2, (1, 4)).float()  # 0 또는 1
print("Mask:", mask)

# 방식 A: 마스크 먼저 적용, 그 다음 softmax
masked_logits_A = logits.masked_fill(mask == 0, float('-inf'))  # 마스크된 위치를 -inf로 채움
prob_A = F.softmax(masked_logits_A, dim=-1)
print("방식 A (마스크 → 소프트맥스):", prob_A)

# 방식 B: 소프트맥스 먼저, 그 다음 마스크 → 재정규화
prob_B_raw = F.softmax(logits, dim=-1)
masked_prob_B = prob_B_raw * mask
prob_B = masked_prob_B / masked_prob_B.sum(dim=-1, keepdim=True)  # 재정규화
print("방식 B (소프트맥스 → 마스크 → 정규화):", prob_B)
