"""def convert_value(value):
    if 'e' in value.lower():
        base, exp = value.lower().split('e')
        if exp.startswith('+'):
            return int(value)
        else:
            return value
    else:
        return value
    
a = convert_value(1.0e-7)
print(a)"""

"""b = 300.0
print(b.is_integer())"""

def convert_value(value):
    # 값이 float이고 정수처럼 보이면 int로 변환
    if isinstance(value, float) and value.is_integer():
        return int(value)
    
    # 값이 딕셔너리이면 재귀적으로 처리
    if isinstance(value, dict):
        return {k: convert_value(v) for k, v in value.items()}
    
    # 값이 리스트이면 각 항목에 대해 변환을 적용
    if isinstance(value, list):
        return [convert_value(v) for v in value]
    
    # 그 외의 경우는 그대로 반환
    return value

# 예시들
values = ["300.0", True, 300.0, 4.5, "Hello", 10, 1.0e+7, 1.0e-4]

converted_values = convert_value(values)
print(converted_values)