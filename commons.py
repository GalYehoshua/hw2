import numpy as np
from matplotlib import pyplot as plt


def print_function(func, x_vals=np.arange(0.5, 10, (10 - 0.5) / 100.0)):
    if isinstance(func, list) and len(func) == len(x_vals):
        plt.plot(x_vals, func)
    else:
        plt.plot(x_vals, [func(x) for x in x_vals])
    plt.show()


def f_noisy(func, x, scaling_factor=1):
    return func(x) + scaling_factor * np.random.uniform(-1, 1, 1)


def der(func, x=np.arange(0, 1, 0.01)):
    # Think of func as a list of numbers where f[i] = f(x[i])
    return 1 / 2 * np.array(func[1:]) - 1 / 2 * np.array(func[:1]) / (x[1:] - x[:1])


def derivative(func_ip, func_im, delta_x):
    return (func_ip - func_im) / (2 * delta_x)

#
# print('TESTING')
# x_range = np.arange(0, 1, 0.01)
# print_function(der([x for x in x_range]), x_range)
# print_function(der([x ** 2 for x in x_range]), x_range)
#
