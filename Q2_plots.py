import matplotlib.pyplot as plt
import numpy as np

from commons import *
from Q2_spline import CubicSplinesInter

scales = [0.001, 0.1, 0.5, 1]


def a_plots():
    plt.subplot(211)
    plt.plot(x_range, f(x_range))
    plt.subplot(212)
    plt.plot(x_range, f(x_range) + 0.1 * noise)
    plt.show()


def b_plots():
    # as num_der is a linear function we can do it directly on the noise.
    x_range = np.linspace(0.5, 10, 99)
    for i, scaling_factor in enumerate(scales):
        plt.subplot(int(f'41{i + 1}'))
        plt.plot(x_range, scaling_factor * der(noise, dx) / noise[:-1])
    plt.show()


def c_plots():
    start, end = 0.5, 10
    inter_points = 99 + 1
    x_range = np.linspace(start, end, inter_points)
    dx = x_range[1] - x_range[0]
    smth_ass_func = f
    for i, scale in enumerate(scales):
        # plt.subplot(int(f'31{i + 1}'))
        f_noise = smth_ass_func(x_range) + scale * noise[:inter_points]
        f_noise_inter_spline = CubicSplinesInter(x_range, f_noise)
        funcs = f_noise_inter_spline.analytical_spline_der()
        x, y = compute_list_of_functions(funcs, np.linspace(start, end, len(funcs) + 1), 20)
        # Removing the original function:
        y -= smth_ass_func(x)

        plt.plot(x, y, color='orange', label="inter data")
        plt.plot(np.linspace(0.5, 10, 100)[:99], scale * der(noise, dx), color='g', label="noise der")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Noise derivation comparison")
        plt.show()


if __name__ == '__main__':
    # a_plots()
    # b_plots()
    c_plots()
