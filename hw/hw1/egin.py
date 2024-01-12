import numpy as np
C = np.array([[-5, 2, 2], [2, -6, 0], [2, 0, -4]])
print(C)
print(np.linalg.eigvals(C))