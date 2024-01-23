import numpy as np

from commons import *
from Q2_plots import noise

scale = 0.1
data = f(x_range) + scale * noise[:len(x_range)]

f_test = x_range ** 3
plt.plot(x_range, f_test)
plt.show()


class SplinesInter:
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
        self.__splines_sec_der()
        self.compute_splines()

    def __splines_sec_der(self):
        # for now assuming points dx is constant
        n = len(self.data) - 2
        dx = self.points_dx[0]
        b_vec = (self.data[:-2] - 2 * self.data[1:-1] + self.data[2:]) * 6 / dx

        dx_mat = dx * np.diag(np.ones(n - 1), 1) \
                 + 4 * dx * np.diag(np.ones(n)) \
                 + dx * np.diag(np.ones(n - 1), -1)
        self._sec_ders = np.concatenate((np.zeros(1), np.dot(np.linalg.inv(dx_mat), b_vec), np.zeros(1)))

    def __compute_coefficients(self):
        dx = self.dx
        self.alphas = self.__splines_sec_der()[1:] / (6 * dx)
        self.betas = -self.__splines_sec_der() / (6 * dx)
        self.gammas = (-self.__splines_sec_der()[1:] * dx * dx + 6 * self.data[1:]) / (6 * dx)
        self.etas = (self.__splines_sec_der() * dx * dx - 6 * self.data) / (6 * dx)

    def sec_ders(self):
        return self._sec_ders

    def compute_splines(self):
        self.__compute_coefficients()
        q = self.inter_points
        splines = []
        for i in range(len(q) - 1):
            spline = lambda x: self.alphas[i] * (x - q[i]) ** 3 \
                               + self.betas[i] * (x - q[i + 1]) ** 3 \
                               + self.gammas[i] * (x - q[i]) \
                               + self.etas[i] * (x - q[i + 1])
            splines.append(spline)
        self.splines = splines

    def full_spline_data(self):
        x = self.inter_points
        full_spline = np.array(x[0], x[-1], )
        splines = self.splines
        for i in range(len(x_range) - 1):
            curr_spline = splines[i]
            full_spline = np.concatenate((full_spline, curr_spline(np.arange(x[i], x[i + 1], (x[i + 1] - x[i]) / 10))))





print('Splines Testing')
test_splines = SplinesInter(data, x_range)
# print(splines_inter.sec_ders())

test_splines = SplinesInter(f_test, x_range)
print(test_splines.sec_ders())
