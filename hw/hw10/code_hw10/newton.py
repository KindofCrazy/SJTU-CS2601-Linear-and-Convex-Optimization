import numpy as np

def newton(fp, fpp, x0, tol=1e-5, maxiter=100000):
	"""
	fp: function that takes an input x and returns the gradient of f at x
	fpp: function that takes an input x and returns the Hessian of f at x
	x0: initial point
	tol: toleracne parameter in the stopping crieterion. Newton's method stops 
	     when the 2-norm of the gradient is smaller than tol
	maxiter: maximum number of iterations

	This function should return a list of iterates x_k produced by each iteration
	"""
	x_traces = [np.array(x0)]
	x = np.array(x0)
	#   START OF YOUR CODE

	while np.linalg.norm(fp(x)) > tol and len(x_traces) < maxiter:
		x = x - np.linalg.inv(fpp(x)) @ fp(x)
		x_traces.append(x)


	#	END OF YOUR CODE

	return x_traces 


def newton_eq(f, fp, fpp, x0, A, b, initial_stepsize=1.0, 
			  alpha=0.5, beta=0.5, tol=1e-5, maxiter=100000):
	"""
	f: function that takes an input x an returns the value of f at x
	fp: function that takes an input x and returns the gradient of f at x
	fpp: function that takes an input x and returns the Hessian of f at x
	A, b: constraint A x = b
	x0: initial feasible point
	initial_stepsize: initial stepsize used in backtracking line search
	alpha: parameter in Armijo's rule 
				f(x + t * d) > f(x) + t * alpha * f(x) @ d
	beta: constant factor used in stepsize reduction
	tol: toleracne parameter in the stopping crieterion. Gradient descent stops 
	     when the 2-norm of the Newton direction is smaller than tol
	maxiter: maximum number of iterations in outer loop of damped Newton's method.

	This function should return a list of the iterates x_k, a list of setpsizes
	"""
	x_traces = [np.array(x0)]
	stepsize_traces = []
	x = np.array(x0)
	#   START OF YOUR CODE

	while len(x_traces) < maxiter:
		m1 = np.concatenate((fpp(x), A.T), axis=1)
		m2 = np.concatenate((A, np.zeros(1).reshape([1,1])), axis=1)
		m = np.concatenate((m1, m2), axis=0)

		s = np.linalg.solve(m, np.concatenate((-fp(x), np.zeros(1).reshape([1,1])), axis=0))
		d = s[:2]
		t = 1
		while f(x+t*d) > f(x) + alpha*t*fp(x).T*d:
			t = beta*d
		x = x + t*d
		x_traces.append(x)
		stepsize_traces.append(t)
		if np.linalg.norm(d) <= tol:
			break
	#	END OF YOUR CODE

	return x_traces, stepsize_traces