import numpy as np
from matplotlib import pyplot as plt

from commons import print_function


def f(x: float):
    return np.sin(x - x ** 2) / x


def find_all_roots_bisection(func, start=0.5, end=7, epsilon=10 ** -4):
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

        print(f"looking for roots in range {low}, {high}")
        current = -1
        while (high - low) >= epsilon:
            # Find middle point
            current = (low + high) / 2
            # Check if middle point is root
            if abs(func(current)) <= epsilon:
                print("here", f(current), current)
                return current
            # Decide the side to repeat the steps
            if func(current) * func(low) < 0:
                high = current
            else:
                low = current
        print(f"left with {low}, {high}, {current}, {f(current)}")
        return

    roots = set()
    step_away_from_root = 10

    def recursive_bisection(low, high):
        if high - low >= epsilon:
            current_root = bisection(low, high)
            if current_root:
                roots.add(current_root)
                recursive_bisection(low, current_root - step_away_from_root * epsilon)
                recursive_bisection(current_root + step_away_from_root * epsilon, high)

    recursive_bisection(start, end)
    return roots


print(sorted(list(find_all_roots_bisection(f, start=0.5, end=10, epsilon=10 ** -4))))
print_function(f)