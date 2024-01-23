import numpy as np
from matplotlib import pyplot as plt

dx = (10 - 0.5) / 100
x_range = np.linspace(0.5, 10, 101)


def f_noisy(func, x, scaling_factor=1):
    return func(x) + scaling_factor * np.random.uniform(-1, 1, 1)


def f(x: float):
    return np.sin(x - x ** 2) / x


def der(func, dx):
    return (func[1:] - func[:-1]) / (2 * dx)


def derivative(func_ip, func_im, delta_x):
    return (func_ip - func_im) / (2 * delta_x)


def find_all_roots(start, end, method, epsilon=1e-6, step_away_from_root=10):
    roots = set()

    def recursive_bisection(low, high):
        if high - low >= epsilon:
            current_root = method(low, high)
            if current_root:
                roots.add(current_root)
                recursive_bisection(low, current_root - step_away_from_root * epsilon)
                recursive_bisection(current_root + step_away_from_root * epsilon, high)

    recursive_bisection(start, end)
    return roots
