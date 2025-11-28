# 원래 데이터
type1 = [0.1814, 0.3615, 0.3334, 0.0892, 0.0197, 0.0148]
type2 = [0.2296, 0.1848, 0.314, 0.1869, 0.0471, 0.0376]
type3 = [0.6562, 0.2352, 0.0568, 0.0181, 0.0157, 0.018]

# 각 type의 합을 구하고, 그 값으로 각 항목을 나누어 비율을 맞춰줍니다.
sum_type1 = sum(type1)
sum_type2 = sum(type2)
sum_type3 = sum(type3)

# 비율 조정
type1_normalized = [x / sum_type1 for x in type1]
type2_normalized = [x / sum_type2 for x in type2]
type3_normalized = [x / sum_type3 for x in type3]

# 결과 확인
print("Normalized Type1:", type1_normalized)
print("Normalized Type2:", type2_normalized)
print("Normalized Type3:", type3_normalized)