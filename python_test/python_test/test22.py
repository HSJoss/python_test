import re
class King:
    pass

class Queen:
    pass

name = "ALE/King-v5"  # or "king-v1", "Queen-v2", etc.

# 1. 대소문자 고려해서 클래스 이름 추출 (첫 알파벳 대문자로 시작하는 단어 추출)
match = re.search(r"([A-Z][a-zA-Z0-9_]*)", name)

if not match:
    raise ValueError(f"Could not extract class name from '{name}'")

class_name = match.group(1)  # 'King' or 'Queen' 등

print(class_name)