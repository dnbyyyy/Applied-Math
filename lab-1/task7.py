from task6 import a, b, h, first_func, second_func, sum_analytics_first, sum_analytics_second
from matplotlib import pyplot
from task5 import center_sum, trapezoid_sum, parabolic_sum
import numpy


def get_deviations(values, method, function, analytics):
    return [abs(method(function, numpy.linspace(a, b, n * int((b - a) / h) + 1), h / n) - analytics(a, b)) for
            n in values]


values = [2, 4, 8, 16]
deviations = [[[get_deviations(values, center_sum, first_func, sum_analytics_first), "center sums"],
               [get_deviations(values, trapezoid_sum, first_func, sum_analytics_first), "trapezoid sums"],
               [get_deviations(values, parabolic_sum, first_func, sum_analytics_first), "parabolic sums"]],
              [[get_deviations(values, center_sum, second_func, sum_analytics_second), "center sums"],
               [get_deviations(values, trapezoid_sum, second_func, sum_analytics_second), "trapezoid sums"],
               [get_deviations(values, parabolic_sum, second_func, sum_analytics_second), "parabolic sums"]]]

steps = [h / 2 ** i for i in range(4)]
_, axis = pyplot.subplots(1, len(deviations), figsize=(20, 4))
for iteration_dev in range(len(deviations)):
    for method in deviations[iteration_dev]:
        axis[iteration_dev].plot(steps, method[0], 'o-', label=method[1])
    axis[iteration_dev].grid()
    axis[iteration_dev].legend()
    axis[iteration_dev].set(xlabel="step $h$", ylabel="deviation",
                            title=f"deviation function {iteration_dev + 1}",
                            xticks=steps)
pyplot.show()
