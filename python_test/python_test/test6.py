"""words = ["mango", "applemango"]

if any("apple" in word for word in words):
    print("hello")"""

## 예시 값 설정
        #self.args = type('', (), {})()  # 임시 객체를 만들어 args 사용

import torch
if torch.tensor([3])==3:
    print("hello")

import torch

words = ["apple", "mango", "applemango", "applekiwi"]

# 'apple'이 포함된 단어들의 인덱스를 찾기
indices = [index for index, word in enumerate(words) if "apple" in word]

k = torch.tensor([3])

print(indices)

# k가 indices에 포함되어 있으면 "hello"를 출력
if k in indices:  # k.item()은 tensor를 Python 값으로 변환
    print("hello")