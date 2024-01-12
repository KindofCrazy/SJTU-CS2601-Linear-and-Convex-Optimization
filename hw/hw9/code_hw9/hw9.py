import algo9 as algo
import matplotlib.pyplot as plt
import numpy as np
import utils

def f(x):
	#   START OF YOUR CODE

	return x - np.log(x)


#	END OF YOUR CODE

def fp(x):
	#   START OF YOUR CODE

	return 1 - 1 / x


#	END OF YOUR CODE

def fpp(x):
	#   START OF YOUR CODE

	return 1 / (x ** 2)


#	END OF YOUR CODE

x0 = 2.5
path="./"
# use the value you find in part (a)
f_opt = 1
def error(x):
	return f(x) - f_opt

#### call newton_damped()
x_traces,stepsize_traces = algo.newton_damped(f,fp, fpp, x0, alpha=0.1, beta=0.7)
f_value = f(x_traces[-1])
for i in range(len(x_traces)): print("x" + str(i) + " = " + str(x_traces[i]))
print('\nDamped Newton\'s method')
print('  number of iterations:', len(x_traces) - 1)
print('  solution:', x_traces[-1])
print('  value:', f_value)

fig = plt.figure(figsize=(3.5, 2.5))
plt.plot(stepsize_traces, '-o', color='blue')
plt.xlabel('iteration (k)')
plt.ylabel('stepsize')
plt.tight_layout(pad=0.1)
fig.savefig(path + 'nt_damped_ss.pdf')

utils.plot(error, x_traces, path+'nt_error_damped.pdf')
