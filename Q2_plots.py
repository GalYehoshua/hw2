import matplotlib.pyplot as plt
import numpy as np

from commons import *
from Q2_spline import CubicSplinesInter

scales = [0.01, 0.1, 0.5]
noise = np.random.uniform(-1, 1, 100)


def a_plots():
    plt.subplot(311)
    plt.plot(x_range, f(x_range))
    plt.title("function plot")
    plt.grid()
    plt.subplot(313)
    plt.plot(x_range, f(x_range) + 0.26 * noise)
    plt.title("function + noise plot lambda = 0.26")
    plt.grid()
    plt.show()


def b_plots():
    # as num_der is a linear function we can do it directly on the noise.
    x_range = np.linspace(0.5, 10, 99)
    for i, scaling_factor in enumerate(scales[:3]):
        plt.subplot(int(f'51{2 * i + 1}'))
        plt.plot(x_range, scaling_factor * der(noise, dx))
        plt.title(f'noise der with scaling factor {scaling_factor}')
        plt.grid()
    plt.show()


def c_plots():
    start, end = 0.5, 10
    inter_points = 100
    x_range = np.linspace(start, end, inter_points)
    dx = x_range[1] - x_range[0]
    smth_ass_func = f
    for i, scale in enumerate(scales):
        # plt.subplot(int(f'31{i + 1}'))
        f_noise = smth_ass_func(x_range) + scale * np.concatenate([[x] * 1 for x in noise[:inter_points]])
        f_noise_inter_spline = CubicSplinesInter(x_range, f_noise)
        funcs = f_noise_inter_spline.analytical_spline_der()
        x, y = compute_list_of_functions(np.linspace(start, end, len(funcs) + 1), funcs, 20)
        # Removing the original derivative of original function:
        y -= der(smth_ass_func(np.concatenate([x, [end + dx]])), dx)

        plt.plot(x, y, color='orange', label="inter data")
        # Taking der on noise.
        plt.plot(np.linspace(0.5, 10, 100)[:99], scale * der(noise, dx), color='red', label="noise der")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Noise derivation comparison with scaling {scale}")
        plt.show()


if __name__ == '__main__':
    a_plots()
    b_plots()
    c_plots()
    #
    # print("Testing now...")
    # start, end = 0.5, 10
    # x_range = np.linspace(start, end, 100)
    # dx = x_range[1] - x_range[0]
    # no_noise_spline = CubicSplinesInter(x_range, f(x_range))
    # funcs = no_noise_spline.analytical_spline_der()
    # x, y = compute_list_of_functions(np.linspace(start, end, len(funcs) + 1), funcs, 20)
    #
    # plt.plot(x, y, color='orange', label="spline")
    # plt.plot(x[:-1], der(f(x), dx), color='r')
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.title("No noise der spline plot")
    # plt.show()
    #
    #
