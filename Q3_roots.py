import numpy as np
from matplotlib import pyplot as plt


def f(x: float):
    return np.sin(x - x ** 2) / x


def print_function():
    x_vals = np.arange(0, 1, 1 / 100.0)
    plt.plot(x_vals, [f(x) for x in x_vals])
    plt.show()


print_function()