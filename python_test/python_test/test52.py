import torch as th

s_dim_input = []

# if s_dim_input:
#     s_dim_input = th.cat([x.reshape(1 * 5, -1) for x in s_dim_input], dim=1)
# else:
#     s_dim_input = th.empty(1 * 5, 0, device="cpu")  # 빈 입력 처리

s_dim_input = th.cat([x.reshape(1 * 5, -1) for x in s_dim_input], dim=1)    

print(s_dim_input)