import numpy as np
import newton as nt

a = np.array([1,2,2], dtype=float)

def f(x):
	return np.sum(np.exp(a*x))

def fp(x):
	#   START OF YOUR CODE
	return a * np.exp(a*x)
	#	END OF YOUR CODE

def fpp(x):
	#   START OF YOUR CODE
	return np.array([[np.exp(x[0]), 0, 0], [0, 4*np.exp(2*x[1]), 0], [0, 0, 4*np.exp(x[2])]])
	#	END OF YOUR CODE

A = np.array([1,1,1], dtype=float).reshape([1,3])

b = np.array([1], dtype=float)

x0 = np.array([1,0,0], dtype=float)

# x_traces = nt.newton(fp, fpp, x0, maxiter=5)

# for i in range(len(x_traces)):
# 	print('iteration %d: %s' % (i, x_traces[i]))
x_traces, stepsize_traces = nt.newton_eq(f, fp, fpp, x0, A, b)

print('')
for k,x in enumerate(x_traces):
	print('iteration %d: %s' % (k, x))
print('optimal value:', f(x_traces[-1]))
print('step sizes:', stepsize_traces)	