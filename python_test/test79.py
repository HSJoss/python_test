def A():
    q = {
        "state": [],
        "obs": [],
        "avail_actions": [],
    }
    w = {
        "reward": [],
        "terminated": [],
    }
    return q, w

aa = A()[0]
aa["state"].append(3)
print(aa)
aa = A()[0]
print(aa)
