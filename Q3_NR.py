from commons import *


def f(x: float):
    return np.sin(x - x ** 2)


def df(x: float):
    return np.cos(x - x ** 2) * (1 - 2 * x)


def criteria(curr_guess, epsilon):
    if abs(curr_guess) < epsilon:
        return epsilon
    return epsilon * abs(curr_guess)


def newton_raphson(func, der_func, initial_guess, epsilon=1e-8):
    curr_guess = initial_guess
    N_max = 1000
    for i in range(N_max):
        prev_guess = curr_guess
        if abs(der_func(curr_guess)) <= epsilon:
            curr_guess -= 100 * epsilon
            continue

        curr_guess = curr_guess - func(curr_guess) / der_func(curr_guess)

        if abs(curr_guess - prev_guess) < criteria(curr_guess, epsilon):
            return curr_guess

    raise Exception(f"Failed to find root for initial guess {initial_guess} in {N_max} steps")


a = newton_raphson(f, df, 2)
print(a, f(a))

# some roots i know [1, 2.341, 3.056, 3.610, 4.079, 4.49474221253328, 4.870300940353982, 5.216045799580043, 5.54...]
