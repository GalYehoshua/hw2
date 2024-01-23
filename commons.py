import numpy as np
from matplotlib import pyplot as plt

dx = (10 - 0.5) / 100
x_range = np.arange(0.5, 10, dx)


def f_noisy(func, x, scaling_factor=1):
    return func(x) + scaling_factor * np.random.uniform(-1, 1, 1)


def f(x: float):
    return np.sin(x - x ** 2) / x


def der(func, dx):
    return (func[1:] - func[:-1]) / (2 * dx)


def derivative(func_ip, func_im, delta_x):
    return (func_ip - func_im) / (2 * delta_x)
