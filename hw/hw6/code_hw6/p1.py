import numpy as np
import gd
import utils


gamma = 0.001 # set the value of gamma by yourself here
X = np.array([[2, 0], [0, 1], [0, 0]])
y = np.array([3, 2, 2])

def f(x):
	return np.linalg.norm(X@x - y)**2

def fp(x):
	return 2 * X.T @ (X@x - y)

def f_2d(x1, x2):
	return 4*x1**2 + x2**2 - 12*x1 - 4*x2 + 17

x0 = np.array([1.0, 1.0])
stepsize = 0.1 # set step size by yourself here

x_traces = gd.gd_const_ss(fp, x0, stepsize=stepsize)

print('number of iterations:', len(x_traces)-1)

utils.plot_traces_2d(f_2d, x_traces, '2_%s.pdf' % (stepsize))
utils.plot(f, x_traces, '_2_%s.pdf' % (stepsize))
print('x:', x_traces[-1])
print('x:', np.linalg.solve(X.T@X, X.T@y))