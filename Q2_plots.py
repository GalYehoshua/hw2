import matplotlib.pyplot as plt
import numpy as np

from commons import *
from Q2_spline import CubicSplinesInter

scales = [0, 0.01, 0.1, 0.5]
noise = np.random.uniform(-1, 1, 100)

noise = np.array([0.9810986589254769, 0.4628976167325285, 0.41120339341642964, -0.9170630051307067, 0.35777513829657126, -0.7866405776775283, -0.12784856841481385, 0.789715156848324, 0.8406450963032868, -0.5089544801864341, 0.9177952197876706, -0.5206701183086575, 0.46237130432926277, 0.8887852785616936, 0.34667697100243644, -0.9651863514104628, -0.21606211159067357, -0.25113622960695126, 0.8209296910774524, 0.6688468182275995, 0.9406319865743813, 0.6263017412294853, -0.6051255595396487, -0.7685825422254386, -0.7872158920124164, -0.9188478200821013, -0.5836358816131217, 0.4764948245916265, 0.6016677441374514, -0.47087415367047236, 0.17640626226226996, 0.1746147640583664, 0.3750135193584252, 0.2899540315357718, 0.5951578314990436, -0.2638932609222093, -0.026447368684432204, 0.16402048431024174, -0.9363364141084674, -0.20184403799955364, 0.9492362642200747, 0.4239593761544467, -0.23025661307936618, -0.10167204756662507, -0.5377494607049789, -0.4977648602215756, -0.9816839313995429, 0.7254317973281081, -0.09426552560607582, 0.2320876896885844, -0.6516812826241087, -0.48734205751512927, 0.9712976382256033, 0.7294015094604782, 0.13724189716421797, 0.3606024550817013, 0.14550573152561874, -0.16943954532631222, -0.871997314641801, 0.8978729491283062, -0.35576249916877445, 0.12152964421191337, -0.004896692830080207, -0.2009096401117696, -0.08634604623262887, 0.7045551018294158, 0.78881213237206, -0.114124936145783, -0.32994392648246573, 0.9286586443998734, -0.8844823831785349, 0.9801514416118702, -0.10949641592506398, 0.8659389170892469, 0.13117201572420556, -0.5213807725773236, -0.6165416778995705, -0.575685477183258, -0.3316142337764971, -0.5275323304158461, 0.4818110767904378, 0.5230634777744227, -0.43186856956779596, -0.6579092479527271, 0.606282619375575, -0.8206638139359619, -0.043232382638549005, 0.45107582944044067, -0.49527402480717275, 0.3396929570887224, 0.49466036509783184, 0.44603307480754006, 0.46893040795666163, 0.3126871324782283, -0.8542703644450582, 0.937300682752565, -0.30334043433892255, -0.9049778612336032, 0.1799150199250923, 0.5408700260694022])


def a_plots():
    plt.subplot(311)
    plt.plot(x_range, f(x_range))
    plt.title("function plot")
    plt.grid()
    plt.subplot(313)
    plt.plot(x_range, f(x_range) + 0.26 * noise)
    plt.title("function + noise plot lambda = 0.26")
    plt.grid()
    plt.show()


def b_plots():
    # as num_der is a linear function we can do it directly on the noise.
    x_range = np.linspace(0.5, 10, 99)
    for i, scaling_factor in enumerate(scales[:3]):
        plt.subplot(int(f'51{2 * i + 1}'))
        plt.plot(x_range, scaling_factor * der(noise, dx))
        plt.title(f'noise der with scaling factor {scaling_factor}')
        plt.grid()
    plt.show()


def c_plots():
    start, end = 0.5, 10
    inter_points = 100
    x_range = np.linspace(start, end, inter_points)
    dx = x_range[1] - x_range[0]
    smth_ass_func = f
    for i, scale in enumerate(scales):
        # plt.subplot(int(f'31{i + 1}'))
        f_noise = smth_ass_func(x_range) + scale * noise  # np.concatenate([[x] * 1 for x in noise[:inter_points]])
        f_noise_inter_spline = CubicSplinesInter(x_range, f_noise)
        funcs = f_noise_inter_spline.analytical_spline_der()
        x, y = compute_list_of_functions(np.linspace(start, end, len(funcs) + 1), funcs, 20)
        # Removing the original derivative of original function:
        y -= der(smth_ass_func(np.concatenate([x, [end + dx]])), dx)

        plt.plot(x, y, color='orange', label="inter data")
        # Taking der on noise.
        plt.plot(np.linspace(0.5, 10, 100)[:99], scale * der(noise, dx), color='red', label="noise der")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Noise derivation comparison with scaling {scale}")
        plt.show()


if __name__ == '__main__':
    # a_plots()
    # b_plots()
    # c_plots()

    print("Testing now...")
    start, end = 0.5, 10
    x_range = np.linspace(start, end, 100)
    dx = x_range[1] - x_range[0]
    no_noise_spline = CubicSplinesInter(x_range, f(x_range))
    funcs = no_noise_spline.splines
    x, y = compute_list_of_functions(np.linspace(start, end, len(funcs) + 1), funcs, 20)

    plt.plot(x, y, color='orange', label="spline")
    plt.plot(x, f(x), color='r')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("No noise spline plot")
    plt.show()


