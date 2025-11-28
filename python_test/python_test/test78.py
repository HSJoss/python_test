terminated = [False, False, True, False]
truncated = [True, False, False, False]

envs_not_done = [e_idx for e_idx, (term, trunc) in enumerate(zip(terminated, truncated)) if not (term or trunc)]

print(envs_not_done)