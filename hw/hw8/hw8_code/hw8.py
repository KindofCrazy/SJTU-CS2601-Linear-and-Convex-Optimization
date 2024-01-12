import numpy as np
import algo
import utils
import matplotlib.pyplot as plt

def f(x):
	return f_2d(x[0], x[1])

def fp(x):
    #   START OF YOUR CODE
    return np.exp(-0.1) * np.array([np.exp(x[0] + 3*x[1]) + np.exp(x[0] - 3*x[1]) - np.exp(-x[0]), 3 * (np.exp(x[0] + 3*x[1]) - np.exp(x[0] - 3*x[1]))])


#	END OF YOUR CODE

def fpp(x):
    #   START OF YOUR CODE
    return np.exp(-0.1) * np.array([[np.exp(x[0] + 3*x[1]) + np.exp(x[0] - 3*x[1]) + np.exp(-x[0]), 3 * (np.exp(x[0] + 3*x[1]) - np.exp(x[0] - 3*x[1]))], [3 * (np.exp(x[0] + 3*x[1]) - np.exp(x[0] - 3*x[1])), 9 * (np.exp(x[0] + 3*x[1]) + np.exp(x[0] - 3*x[1]))]])
    pass


#	END OF YOUR CODE

def f_2d(x1, x2):
	return np.exp(x1+3*x2-0.1) + np.exp(x1 - 3*x2 - 0.1) + np.exp(-x1-0.1)

# use the value you find in part (a)
x_opt = np.array([np.log(np.sqrt(0.5)), 0.0])
f_opt = f(x_opt)
v_opt = np.linalg.eigvals(fpp(x_opt))
print('eigenvalues at x_opt =', x_opt, ':', v_opt)
#

def error(x):
	return f(x) - f_opt


x0 = np.array([2.0, 1.0])
print('eigenvalues at', x0, ':', np.linalg.eigvals(fpp(x0)))
path = './'

#### call Armijo for P1(b) and P1(c)
run_armijo= True
if run_armijo:
    x_traces_armijo, stepsize_traces, num_iter_inner = algo.gd_armijo(f, fp, x0, alpha=0.1, beta=0.7)
    f_value_armijo = f(x_traces_armijo[-1])

    print('\ngradient descent with Armijo')
    print('  number of iterations in outer loop:', len(x_traces_armijo)-1)
    print('  total number of iterations in inner loop:', num_iter_inner)
    print('  solution:', x_traces_armijo[-1])
    print('  value:', f_value_armijo)

    utils.plot_traces_2d(f_2d, x_traces_armijo, path+'gd_traces_armijo.pdf')
    utils.plot(error, x_traces_armijo, path+'gd_error_armijo.pdf')

    fig = plt.figure(figsize=(3.5,2.5))
    plt.plot(stepsize_traces, '-o', color='blue')
    plt.xlabel('iteration (k)')
    plt.ylabel('stepsize')
    plt.tight_layout(pad=0.1)
    fig.savefig(path+'gd_armijo_ss.pdf')


#### call Newton for P1(d) and P1(e)
run_newton = True
if run_newton:
    x_traces = algo.newton(fp, fpp, x0)
    f_value = f(x_traces[-1])

    print('\nNewton\'s method')
    print('  number of iterations:', len(x_traces) - 1)
    print('  solution:', x_traces[-1])
    print('  value:', f_value)

    utils.plot_traces_2d(f_2d, x_traces, path + 'nt_traces.pdf')
    utils.plot(error, x_traces, path + 'nt_error.pdf')