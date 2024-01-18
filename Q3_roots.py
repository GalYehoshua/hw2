import numpy as np
from matplotlib import pyplot as plt

from commons import print_function


def f(x: float):
    return np.sin(x - x ** 2) / x


def find_all_roots_bisection(func, start=0, end=100, epsilon=10 ** -4):
    def alter_high_if_required(low, high, step=epsilon):
        sgn = np.sign(func(low))
        while sgn * func(high) >= 0 and (high - low) >= epsilon:
            # TODO: consider grad decent.
            high -= epsilon
        return high

    def bisection(low, high):
        # TODO: make a test outside to determine low and high
        high = alter_high_if_required(low, high)
        if func(low) * func(high) >= 0:
            print("Issues with end points\n")
            return

        current = low
        while (high - low) >= epsilon:
            # Find middle point
            current = (low + high) / 2
            # Check if middle point is root
            if abs(func(current)) < epsilon:
                print("here", f(current))
                return current
            # Decide the side to repeat the steps
            if func(current) * func(low) < 0:
                high = current
            else:
                low = current

    roots = {}
    step_away_from_root = 0.1
    flag = True
    while flag:
        current_root = bisection(start, end)


find_all_roots_bisection(func=f)

print_function(f)
