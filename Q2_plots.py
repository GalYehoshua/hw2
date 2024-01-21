from commons import *


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
        plt.subplot(int(f'41{i + 1}'))
        plt.plot(x_range, scaling_factor * der(noise, dx) / noise[:-1])
    plt.show()


a_plots()
b_plots()
