import numpy as np
import gd
import utils
import matplotlib.pyplot as plt

# x: features of data samples, y: categories of data samples
x = np.array([[1,1.5], [1.2, 2.5], [1,3.5], [2,2.25], [1.8, 3], [2.5,4], [3,1.9], 
	          [1.5, .5], [2.5, .8], [2.8, .3], [3.2, .3], [3, .8], [3.8, 1], [4,2], [1.8,1.8]])
# add bias term
x = np.append(x, np.ones((15,1)), axis=1)
y = np.append(np.ones((7,)), np.zeros((8,)))

# x.shape = (15, 3), y.shape = (15,)
print (x.shape, y.shape)

# sigmoid function
def sigma(theta):
	# implement the sigmoid function h_\theta(x) here
	result = []
	for xi in x:
		result.append(1 / (1 + np.exp(-theta.dot(xi))))
	return result

def fp(theta):
	# implement the function for computing gradient here
	s = sigma(theta)
	g = 0
	for i in range(len(x)):
		g += (s[i] - y[i]) * x[i]
	return g

# implement optimization by gradient descent here
theta0 = np.array([0.0, 0.0, 0.0])
stepsize = 0.1
theta_trace = gd.gd_const_ss(fp, theta0, stepsize=stepsize)

# compute accuracy
theta = theta_trace[-1] # last theta of the trace
print('theta:', theta)
print('number of iterations', len(theta_trace) - 1)
print (sum(np.around(sigma(theta)) == y) / float(x.shape[0]))

# visualization
xp = np.linspace(min(x[:, 0]), max(x[:, 0]), 100)
yp = -(theta[0] * xp + theta[2]) / theta[1]

idx0 = np.where(y == 0) 
idx1 = np.where(y == 1)

plt.figure(figsize=(3, 3))

plt.plot(x[idx0[0], 0], x[idx0[0], 1], 'rx')
plt.plot(x[idx1[0], 0], x[idx1[0], 1], 'go')
plt.plot(xp, yp, '-b')

plt.tight_layout()
plt.savefig('plot.pdf')
