import numpy as np
from matplotlib import pyplot as plt


def f(x: float):
    return np.sin((100 * x) ** 0.5) ** 2


def print_function():
    x_vals = np.arange(0, 1, 1 / 100)
    plt.plot(x_vals, [f(x) for x in x_vals])
    plt.show()


def trapeziod_integrals(err=10 ** -6, func=f):
    integrals = [0, 1 * (func(1) + func(0))]
    i = 1  # number of subdivision will be 2 ** i

    # calc the width of the i'th iteration, i=0 is full interval
    def width(iteration):
        return 1.0 / 2 ** iteration

    assert width(1) == 1/2

    while True:
        new_integral = 0.5 * integrals[i] + width(i) * sum([func(k * width(i)) for k in range(1, 2 ** i, 2)])
        integrals.append(new_integral)
        if (integrals[i + 1] - integrals[i]) / 3 < err:
            return integrals[-1]

        if i == 1000:
            print('finish at step 1000 with approx. err', (integrals[i + 1] - integrals[i]) / 3)
            return integrals[-1]

        i += 1


print(trapeziod_integrals())

