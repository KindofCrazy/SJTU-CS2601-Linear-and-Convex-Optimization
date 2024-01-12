import numpy as np


def newton_damped(f, fp, fpp, x0, initial_stepsize=1.0, alpha=0.1, beta=0.7, tol=1e-5, maxiter=100000):
	"""
	f: function that takes an input x an returns the value of f at x
	fp: function that takes an input x and returns the gradient of f at x
	fpp: function that takes an input x and returns the Hessian of f at x
	x0: initial point in gradient descent
	initial_stepsize: initial stepsize used in backtracking line search
	alpha: parameter in Armijo's rule
				f(x - t * f'(x)) > f(x) - t * alpha * ||f'(x)||^2
	beta: constant factor used in stepsize reduction
	tol: toleracne parameter in the stopping crieterion. Gradient descent stops
	     when the 2-norm of the gradient is smaller than tol
	maxiter: maximum number of iterations in gradient descent.

	This function should return a list of the sequence of approximate solutions
	x_k produced by each iteration and the total number of iterations in the inner loop
	"""
	x_traces = [np.array(x0)]
	stepsize_traces = []

	x = np.array(x0)
	#   START OF YOUR CODE

	while np.linalg.norm(fp(x)) > tol and len(x_traces) <= maxiter:
		d = -fp(x) / fpp(x)			
		# d = -np.linalg.inv(fpp(x)) @ fp(x)

		t = 1
		while f(x + t * d) > f(x) + alpha * t * fp(x) * d:
			t *= beta
		x = x + t * d
		x_traces.append(x)
		stepsize_traces.append(t)

	#   END OF YOUR CODE
	return x_traces, stepsize_traces