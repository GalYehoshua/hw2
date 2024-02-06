import numpy as np
from matplotlib import pyplot as plt


def f(x: float):
    return np.sin((100 * x) ** 0.5) ** 2


def print_function():
    x_vals = np.linspace(0, 1, 101)
    plt.plot(x_vals, [f(x) for x in x_vals])
    plt.show()


# calc the width of the i'th iteration, i=0 is full interval
def width(iteration):
    return 1.0 / 2 ** iteration


def trapeziod_integrals(err=10 ** -6, func=f):
    integrals = [0, 1 * 0.5 * (func(1) + func(0))]
    i = 1  # number of subdivision will be 2 ** i

    assert width(1) == 1 / 2

    while True:
        new_integral = 0.5 * integrals[-1] + width(i) * sum([func(k * width(i)) for k in range(1, 2 ** i, 2)])
        integrals.append(new_integral)
        if abs(integrals[i + 1] - integrals[i]) / 3 < err:
            print(i, integrals[:], (integrals[i + 1] - integrals[i]) / 3)
            return integrals[-1]

        if i == 1000:
            print('finish at step 1000 with approx. err', (integrals[i + 1] - integrals[i]) / 3)
            return integrals[-1]

        i += 1


def romberg(err=1e-6, func=f, start=0, end=1):
    trapeziod_integrals = {1: 0.5 * (func(start) + func(end))}
    trapeziod_integrals[2] = 0.5 * trapeziod_integrals[1] + 0.5 * (func(0.5))
    romberg_integrals = {(1, 1): trapeziod_integrals[1],
                         (2, 1): trapeziod_integrals[2]}

    romberg_integrals[(2, 2)] = romberg_integrals[(2, 1)] \
                                + 1 / 3 * (romberg_integrals[(2, 1)] - romberg_integrals[(1, 1)])
    i = 3
    while True:
        # computing trapeziod integrals using eq 2; note the shift due to 0 base.
        trapeziod_integrals[i] = 0.5 * trapeziod_integrals[i - 1] \
                                 + width(i - 1) * sum([func(k * width(i - 1)) for k in range(1, 2 ** (i - 1), 2)])
        # setting R_i1 to be I_i
        romberg_integrals[(i, 1)] = trapeziod_integrals[i]
        # computing refined romberg integrals using eq 3
        for m in range(1, i):
            romberg_integrals[(i, m + 1)] = romberg_integrals[(i, m)] \
                                            + (romberg_integrals[(i, m)] - romberg_integrals[(i - 1, m)]) / (4 ** m - 1)

        # estimate the err by eq 4.
        estimate_err = (romberg_integrals[(i, i - 1)] - romberg_integrals[(i - 1, i - 1)]) / (4 ** (i - 1) - 1)
        if abs(estimate_err) < err:
            print(trapeziod_integrals)
            print(romberg_integrals)
            return i, romberg_integrals[(i, i)], estimate_err
        i += 1

        # computation did not converge after 1000 iterations, halt! you may cry now :(
        if i == 1000:
            print('finish at step 1000 with approx. err', estimate_err)
            return romberg_integrals


print(trapeziod_integrals())

# print_function()
print(romberg())
