import numpy as np

def gd_armijo(f, fp, x0, initial_stepsize=1.0, alpha=0.5, beta=0.5, tol=1e-5, maxiter=100000):
	"""
	f: function that takes an input x an returns the value of f at x
	fp: function that takes an input x and returns the derivative of f at x
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
	tot_num_inner_iter = 0
	tot_num_outer_iter = 0
	x = np.array(x0)
	#   START OF YOUR CODE

	while np.linalg.norm(fp(x)) > tol and tot_num_outer_iter < maxiter:
		t = initial_stepsize
		gd = fp(x)
		while f(x - t * gd) > f(x) - alpha * t * (np.linalg.norm(gd) ** 2):
			t = beta * t
			tot_num_inner_iter += 1
		x = x - t * gd
		x_traces.append(x)
		stepsize_traces.append(t)
		tot_num_outer_iter += 1

	#	END OF YOUR CODE

	return x_traces, stepsize_traces, tot_num_inner_iter


def newton(fp, fpp, x0, tol=1e-5, maxiter=100000):
	"""
	fp: function that takes an input x and returns the gradient of f at x
	fpp: function that takes an input x and returns the Hessian of f at x
	x0: initial point
	tol: toleracne parameter in the stopping crieterion. Newton's method stops
		when the 2-norm of the gradient is smaller than tol
	maxiter: maximum number of iterations

	This function should return a list of the sequence of approximate solutions
	x_k produced by each iteration
	"""
	x_traces = [np.array(x0)]
	tot_num_iter = 0
	x = np.array(x0)
	#   START OF YOUR CODE

	while np.linalg.norm(fp(x)) > tol and tot_num_iter < maxiter:
		x = x - np.linalg.inv(fpp(x)) @ fp(x)
		x_traces.append(x)
		tot_num_iter += 1

	#	END OF YOUR CODE

	return x_traces