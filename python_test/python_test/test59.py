def sum_first_dimension(shapes):
    # 첫 번째 차원만 더하고 나머지 차원은 그대로 유지
    result_shape = list(shapes[0])  # 첫 번째 shape을 기준으로 초기화

    # 첫 번째 차원만 더함
    for shape in shapes[1:]:
        result_shape[0] += shape[0]
    
    return tuple(result_shape)

# 예시 1
input_vshape_1 = [(3, 84, 84), (5, 84, 84), (2, 84, 84)]
result_1 = sum_first_dimension(input_vshape_1)
print(result_1)  # 출력: (8, 84, 84)

# 예시 2
input_vshape_2 = [(10,), (14,), (3,)]
result_2 = sum_first_dimension(input_vshape_2)
print(result_2)  # 출력: (24,)

input_vshape_3 = [(2, 84, 84)]
result_3 = sum_first_dimension(input_vshape_3)
print(result_3)