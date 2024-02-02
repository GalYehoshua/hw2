import numpy as np

from commons import *
from Q2_spline import CubicSplinesInter

scales = [0.1, 0.5, 1]


def a_plots():
    plt.subplot(211)
    plt.plot(x_range, f(x_range))
    plt.subplot(212)
    plt.plot(x_range, f(x_range) + 0.1 * noise[:100])

    # plt.plot(x_range, np.gradient(f(x_range), 2 * dx))
    # plt.subplot(313)
    # plt.plot(x_range[1:], der(f(x_range), dx))
    plt.show()


def b_plots():
    x_range = np.linspace(0.5, 10, 99)
    for i, scaling_factor in enumerate(scales):
        plt.subplot(int(f'41{i + 1}'))
        plt.plot(x_range, scaling_factor * der(noise, dx) / noise[:-1])
    plt.show()


def c_plots():
    start, end = 0.5, 10
    x_range = np.linspace(start, end, 100)
    for i, scale in enumerate(scales):
        plt.subplot(int(f'41{i + 1}'))
        f_noise = f(x_range) + scale * noise
        curr_spline = CubicSplinesInter(f_noise, x_range)
        x, y = compute_list_of_functions(curr_spline.analytical_spline_der(), np.linspace(start, end, 10), 11)
        plt.plot(x, y)
        plt.show()


if __name__ == '__main__':
    a_plots()
    b_plots()
