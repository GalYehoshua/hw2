import matplotlib.pyplot as plt
import numpy as np

from commons import *
from Q2_spline import CubicSplinesInter

scales = [0.1, 0.5, 1]


def a_plots():
    plt.subplot(211)
    plt.plot(x_range, f(x_range))
    plt.subplot(212)
    plt.plot(x_range, f(x_range) + 0.1 * noise)
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
    for i, scale in enumerate(scales[:1]):
        plt.subplot(int(f'31{i + 1}'))
        f_noise = f(x_range) + scale * noise
        curr_spline = CubicSplinesInter(x_range, f_noise)
        funcs = curr_spline.analytical_spline_der()
        x, y = compute_list_of_functions(funcs, np.linspace(start, end, len(funcs) + 1), 11)
        plt.plot(x, y)
        plt.show()


def c2_plots():
    start, end = 0.5, 10
    x_range = np.linspace(start, end, 100)
    noise_spline_inter = CubicSplinesInter(x_range, noise)
    noise_spline = noise_spline_inter.splines

    # noise inter
    plt.subplot(211)
    x, y = compute_list_of_functions(noise_spline, np.linspace(start, end, len(noise_spline) + 1), 4)
    plt.plot(x, y/y[0])

    print(y[0:33])
    print(noise[0:33])

    plt.subplot(212)
    der_noise = noise_spline_inter.analytical_spline_der()
    x, y = compute_list_of_functions(der_noise, np.linspace(start, end, len(der_noise) + 1), 4)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    # a_plots()
    # b_plots()
    c2_plots()
