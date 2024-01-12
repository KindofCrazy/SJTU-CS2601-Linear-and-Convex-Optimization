import numpy as np
import cvxpy as cp
from cvxpy import maximum

# Create two scalar optimization variables.
w = cp.Variable(2)
t = 10
s = np.ones(3)
X = np.array([[2, 0], [0, 1], [0, 0]])
y = np.array([3, 2, 2])

# Create two constraints.
constraints = [
    (cp.norm1(w) ** 2) <= t
]

# Form objective.
obj = cp.Minimize((cp.norm2(X @ w - y)) ** 2)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print(f"optimal var: w:{w.value}")