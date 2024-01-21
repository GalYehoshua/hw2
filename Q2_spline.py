import numpy as np

from commons import *


def cubic_spline(data, dx):
    n = len(data) - 2
    b_vec = (data[:-2] - 2 * data[1:-1] + data[2:]) * 6 / dx
    dx_mat = dx * np.diag(np.ones(n - 1), 1) \
             + 4 * dx * np.diag(np.ones(n)) \
             + dx * np.diag(np.ones(n - 1), -1)
    return np.dot(np.linalg.inv(dx_mat), b_vec)

