import numpy as np

a = [["SFFF", "FHFH", "FFFH", "HFFG"], ["SFFFFFFF", "FFFFFFFF", "FFFHFFFF", "FFFFFHFF", "FFFHFFFF", "FHHFFFHF", "FHFFHFHF", "FFFHFFFG",]]
print(len(a[1]))


import numpy as np
b = np.asarray(a[0], dtype="c")

print(b.shape)