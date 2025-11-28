import torch
import torch.nn as nn

class B(nn.Module):
    def __init__(self):
        super().__init__()  # 반드시 호출
    def forward(self, hidden_state):
        return hidden_state + 3  # 값을 변경한 결과를 반환

class A(nn.Module):
    def __init__(self):
        super().__init__()  # 반드시 호출
        self.hidden_state = torch.tensor(0)  # Tensor로 초기화
        self.net = B()

    def forward(self):
        self.hidden_state = self.net(self.hidden_state)  # 반환값을 다시 저장

model = A()

for _ in range(3):
    model.forward()

print(model.hidden_state)  # 출력: tensor(9)
