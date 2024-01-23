from commons import *

noise = np.random.uniform(-1, 1, 101)


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
    for i, scaling_factor in enumerate([1, 0.1, 0.01]):
        plt.subplot(int(f'41{i + 1}'))
        plt.plot(x_range, scaling_factor * der(noise, dx) / noise[:-1])
    plt.show()


if __name__ == '__main__':
    a_plots()
    b_plots()
