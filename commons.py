import numpy as np
from matplotlib import pyplot as plt


def print_function(func, x_vals=np.arange(0.4, 10, 1 / 100.0)):
    plt.plot(x_vals, [func(x) for x in x_vals])
    plt.show()
