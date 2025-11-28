terminated = [True, True, True, False]
truncated = [False, True, True, True]
done = [e_idx for e_idx, (term, trunc) in enumerate(zip(terminated, truncated)) if not (term or trunc)]

print(done)
print(not done)