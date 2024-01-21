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


print('TESTING')

plt.figure()


def a_plots():
    plt.subplot(311)
    plt.plot(x_range, f(x_range))
    plt.subplot(312)
    plt.plot(x_range, np.gradient(f(x_range), 2 * dx))
    plt.subplot(313)
    plt.plot(x_range[1:], der(f(x_range), dx))
    plt.show()


def b_plots():
    noise = np.random.uniform(-1, 1, 101)
    for i, scaling_factor in enumerate([1, 0.1, 0.01]):
        plt.subplot(int(f'41{i+1}'))
        plt.plot(x_range, scaling_factor * der(noise, dx) / noise[:-1])
    plt.show()


b_plots()
