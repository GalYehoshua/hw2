import abc

from commons import *


class CubicSplinesInter:
    def __init__(self, x, data):
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
        # self.assert_spline()

    def __splines_sec_der(self):
        # for now assuming points dx is constant, which is true for equivalent spaced points
        n = len(self.data) - 2
        dx = self.points_dx[0]
        b_vec = (self.data[:-2] - 2 * self.data[1:-1] + self.data[2:]) * 6

        tri_mat = np.diag(np.ones(n - 1), 1) \
                  + 4 * np.diag(np.ones(n)) \
                  + np.diag(np.ones(n - 1), -1)
        self._sec_ders = np.concatenate((np.zeros(1), np.dot(np.linalg.inv(tri_mat), b_vec), np.zeros(1))) / (dx ** 2)

    def __compute_coefficients(self):
        dx = self.dx
        self.alphas = self.sec_ders()[1:] / (6 * dx)
        self.betas = -self.sec_ders() / (6 * dx)
        self.gammas = -self.sec_ders()[1:] * dx / 6 + self.data[1:] / dx
        self.etas = self.sec_ders() * dx / 6 - self.data / dx

    def sec_ders(self):
        return self._sec_ders

    @staticmethod
    def spline_by_params(a, b, g, e, qi, qi_1):
        def f(x):
            return a * (x - qi) ** 3 + b * (x - qi_1) ** 3 + g * (x - qi) + e * (x - qi_1)
        return f

    @staticmethod
    def der_spline_by_params(a, b, g, e, qi, qi_1):
        def f(x):
            return 3 * a * (x - qi) ** 2 + 3 * b * (x - qi_1) ** 2 + g + e
        return f

    def compute_splines(self):
        q = self.inter_points
        splines = []
        print(f"You will have {len(q) - 1} polys in interpolation")
        for i in range(len(q) - 1):
            # spline = lambda x: self.alphas[i] * ((x - q[i]) ** 3) \
            #                    + self.betas[i] * ((x - q[i + 1]) ** 3) \
            #                    + self.gammas[i] * (x - q[i]) \
            #                    + self.etas[i] * (x - q[i + 1])
            spline = self.spline_by_params(self.alphas[i], self.betas[i], self.gammas[i], self.etas[i], q[i], q[i + 1])
            splines.append(spline)
        self.splines = splines

    def analytical_spline_der(self):
        q = self.inter_points
        splines_der = []
        for i in range(len(q) - 1):
            spline_der = self.der_spline_by_params(self.alphas[i], self.betas[i],
                                                   self.gammas[i], self.etas[i], q[i], q[i + 1])
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
        for i, x in enumerate(self.splines):
            spline_eval = self.splines[i](x)
            if not self.data[i] == spline_eval:
                print("Something is wrong please check")
                print(f"data point at internal point {i}, {x} is {self.data[i]},"
                      f" while splines{i} is {self.splines[i](x)}")


if __name__ == "__main__":
    print('Splines Testing')
    scale = 0.1
    x_range = np.linspace(0.5, 10, 100)
    noise = np.random.uniform(-1, 1, 100)
    data = f(x_range) + scale * noise[:len(x_range)]

    test_splines = CubicSplinesInter(np.linspace(0.5, 10, 100), data)
    # sec der looks fine.
    # print("sec der", test_splines.sec_ders())
    x, y = compute_list_of_functions(test_splines.inter_points, test_splines.splines, 10)

    print("last data is", test_splines.data[-20:], "len data", len(test_splines.data))

    plt.plot(x, y)
    plt.show()
