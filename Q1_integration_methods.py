import numpy as np
from matplotlib import pyplot as plt


def f(x: float):
    return np.sin((100 * x) ** 0.5) ** 2

print("here")
x_vals = np.arange(0,1, 1/100)
plt.plot(x_vals, [f(x) for x in x_vals])
plt.show()
