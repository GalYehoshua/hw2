import matplotlib.pyplot as plt
import numpy as np

from commons import *

scale = 0.1
data = f(x_range) + scale * noise[:len(x_range)]
f_test = x_range ** 2


class CubicSplinesInter:
    def __init__(self, data, x):
        self.data = data
        self.inter_points = x
        self.points_dx = x[1:] - x[:-1]  # x_i+1 - x_i
        self.dx = self.points_dx[0]
        self.splines = []
        self.alphas = []
        self.betas = []
        self.gammas = []
        self.etas = []
        # when creating spline already compute it
        self.__splines_sec_der()
        self.__compute_coefficients()
        self.compute_splines()

    def __splines_sec_der(self):
        # for now assuming points dx is constant
        n = len(self.data) - 2
        dx = self.points_dx[0]
        b_vec = (self.data[:-2] - 2 * self.data[1:-1] + self.data[2:]) * 6

        dx_mat = np.diag(np.ones(n - 1), 1) \
                 + 4 * np.diag(np.ones(n)) \
                 + np.diag(np.ones(n - 1), -1)
        self._sec_ders = np.concatenate((np.zeros(1), np.dot(np.linalg.inv(dx_mat), b_vec), np.zeros(1))) / (dx ** 2)

    def __compute_coefficients(self):
        dx = self.dx
        self.alphas = self.sec_ders()[1:] / (6 * dx)
        self.betas = -self.sec_ders() / (6 * dx)
        self.gammas = (-self.sec_ders()[1:] * dx * dx + 6 * self.data[1:]) / (6 * dx)
        self.etas = (self.sec_ders() * dx * dx - 6 * self.data) / (6 * dx)

    def sec_ders(self):
        return self._sec_ders

    def compute_splines(self):
        q = self.inter_points
        splines = []
        for i in range(len(q) - 1):
            spline = lambda x: self.alphas[i] * (x - q[i]) ** 3 \
                               + self.betas[i] * (x - q[i + 1]) ** 3 \
                               + self.gammas[i] * (x - q[i]) \
                               + self.etas[i] * (x - q[i + 1])
            splines.append(spline)
        self.splines = splines

    def analytical_spline_der(self):
        q = self.inter_points
        splines_der = []
        for i in range(len(q) - 1):
            spline_der = lambda x: 3 * self.alphas[i] * (x - q[i]) ** 2 \
                                   + 3 * self.betas[i] * (x - q[i + 1]) ** 2 \
                                   + self.gammas[i] \
                                   + self.etas[i]
            splines_der.append(spline_der)
        return splines_der

    # not to use, use compute_list_of_functions() from commons.
    def full_spline_data(self):
        x = self.inter_points
        refinement = 10
        full_x_range = np.linspace(x[0], x[-1], (len(x) - 1) * refinement)
        full_spline = []
        splines = self.splines
        for i in range(len(x_range) - 1):
            curr_spline = splines[i]
            full_spline = np.concatenate((full_spline, curr_spline(np.linspace(x[i], x[i + 1], refinement))))
        return full_x_range, full_spline

    def assert_spline(self):
        for i, x in enumerate(self.inter_points):
            if not self.data[i] == self.splines[i](x):
                print("Something is wrong please check")
                print(f"data point at internal point {i}, {x} is {self.data[i]},"
                      f" while splines{i} is {self.splines[i](x)}")


if __name__ == "__main__":
    splines_inter = CubicSplinesInter(data, x_range)

    # print(splines_inter.sec_ders()[:20])

    # # a test for simple functions, sec der works ok.
    # test_splines = CubicSplinesInter(f_test, x_range)
    # print(test_splines.sec_ders()[:20] / x_range[:20])

    print('Splines Testing')

    test_splines = CubicSplinesInter(np.linspace(0.5, 10, 11) ** 2, np.linspace(0.5, 10, 11))

    x, y = compute_list_of_functions(test_splines.analytical_spline_der(), test_splines.inter_points, 10)
    print(y)

    p4 = test_splines.splines[4]
    print("p4 \n", x, "\n", p4(x))

    print("sec der", test_splines.sec_ders())
    plt.plot(x, y)
    plt.show()
