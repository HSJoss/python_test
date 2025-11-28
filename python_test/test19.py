# For ALE LIST

# 파일 읽기
with open("C:/atari/python_test/a.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 변환 작업
processed_lines = []
for line in lines:
    stripped = line.strip()
    if stripped:  # 빈 줄이 아닌 경우만 처리
        processed_line = f'- "{stripped.lower()}"'
        processed_lines.append(processed_line)

# 파일 쓰기
with open("b.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(processed_lines))