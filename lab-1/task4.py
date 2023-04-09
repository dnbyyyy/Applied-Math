import task3
import numpy
from matplotlib import pyplot


def get_counted_mse(reducer, func):
    argx = numpy.linspace(task3.a, task3.b, reducer * int((task3.b - task3.a) / task3.h) + 1)
    analytic_diff_first = task3.first_func_derivative(argx)
    mse_right_first = sum(
        (x - a) ** 2 for x, a in zip(task3.right_diff(func, argx, task3.h / reducer), analytic_diff_first)) / len(
        analytic_diff_first)
    mse_center_first = sum(
        (x - a) ** 2 for x, a in zip(task3.diff(func, argx, task3.h / reducer), analytic_diff_first)) / len(
        analytic_diff_first)
    return [mse_right_first, mse_center_first]


# counted mse with h/2 h/4 h/8 h/16
mse_right_first_reduced_by_2, mse_center_first_reduced_by_2 = get_counted_mse(2, task3.first_func)
mse_right_first_reduced_by_4, mse_center_first_reduced_by_4 = get_counted_mse(4, task3.first_func)
mse_right_first_reduced_by_8, mse_center_first_reduced_by_8 = get_counted_mse(8, task3.first_func)
mse_right_first_reduced_by_16, mse_center_first_reduced_by_16 = get_counted_mse(16, task3.first_func)

steps = [task3.h / 2 ** i for i in range(5)]
fig, axis = pyplot.subplots(1, 2, figsize=(10, 4))
axis[0].plot(steps,
             [task3.mse_right_first, mse_right_first_reduced_by_2, mse_right_first_reduced_by_4,
              mse_right_first_reduced_by_8, mse_right_first_reduced_by_16],
             'o-', label="right method",
             markersize=8)
axis[1].plot(steps,
             [task3.mse_center_first, mse_center_first_reduced_by_2, mse_center_first_reduced_by_4,
              mse_center_first_reduced_by_8, mse_center_first_reduced_by_16],
             'o-', label="center method",
             markersize=8)
axis[0].grid()
axis[1].grid()
axis[0].legend()
axis[1].legend()
axis[0].set(xlabel="step $h$", ylabel="$mse_{right}$", title="$mse_{right}$  first func", xticks=steps)
axis[1].set(xlabel="step $h$", ylabel="$mse_{center}$", title="$mse_{center}$ first func", xticks=steps)
pyplot.show()
