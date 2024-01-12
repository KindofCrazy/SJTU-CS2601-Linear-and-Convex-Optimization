import numpy as np

x = np.array([[2, 0 ,1/2], [0,1,1],[1/2,1,1/2]])
print(x)
print(np.linalg.eigvals(x))