import numpy as np
from matplotlib import pyplot as plt

x_range = np.linspace(0.5, 10, 100)
dx = x_range[1] - x_range[0]
noise = np.random.uniform(-1, 1, 100)


# was tested and is fine.
def compute_list_of_functions(funcs, boundaries, division):
    """
    :param funcs: a list of funcs
    :param boundaries: list of boundary points for functions, must be of length(funcs) + 1
    :param division: number of points to divide each boundary
    :rtype: tuple, tuple is of range and outputs
    """
    assert len(funcs) + 1 == len(boundaries)
    full_x_range = []
    funcs_outputs = []
    for i, func in enumerate(funcs):
        funcs_outputs = funcs_outputs[:-1] + list(func(np.linspace(boundaries[i], boundaries[i + 1], division)))
        full_x_range = full_x_range[:-1] + list(np.linspace(boundaries[i], boundaries[i + 1], division))

    return np.array(full_x_range), np.array(funcs_outputs)


def f_noisy(func, x, scaling_factor=1):
    return func(x) + scaling_factor * np.random.uniform(-1, 1, 1)


def f(x: float):
    return np.sin(x - x ** 2) / x


def der(func, dx):
    return (func[1:] - func[:-1]) / (2 * dx)


def derivative(func_ip, func_im, delta_x):
    return (func_ip - func_im) / (2 * delta_x)


def find_all_roots(start, end, method, epsilon=1e-6, step_away_from_root=10):
    roots = set()

    def recursive_bisection(low, high):
        if high - low >= epsilon:
            current_root = method(low, high)
            if current_root:
                roots.add(current_root)
                recursive_bisection(low, current_root - step_away_from_root * epsilon)
                recursive_bisection(current_root + step_away_from_root * epsilon, high)

    recursive_bisection(start, end)
    return roots


if __name__ == "__main__":
    print('funcs plot test')
    funcs = [lambda x: np.sin(x), lambda x: np.sin(x), lambda x: np.sin(x), lambda x: np.sin(x), lambda x: np.sin(x)]

    x, y = compute_list_of_functions(funcs, np.linspace(0, 26, len(funcs) + 1), 100)
    print(len(x))
    plt.plot(x, y)
    plt.show()
