from collections import defaultdict

a = defaultdict(dict)
a["d"]["k"] = 3
print(a)
print(a["d"])  