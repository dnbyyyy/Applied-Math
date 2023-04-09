from task5 import trapezoid_sum, parabolic_sum, left_sum, right_sum, center_sum
import numpy
from matplotlib import  pyplot


def first_func(x):
    return numpy.e ** numpy.sqrt(x) * numpy.sqrt(x)


def second_func(x):
    return numpy.log(x) + numpy.e * numpy.cos(x)


def sum_analytics_first(a, b):
    return (2 * numpy.e ** numpy.sqrt(b) * (b - 2 * numpy.sqrt(b) + 2)) - (2 * numpy.e ** numpy.sqrt(a) * (a - 2 * numpy.sqrt(a) + 2))


def sum_analytics_second(a, b):
    return (b * (numpy.log(b) - 1) + numpy.e * numpy.sin(b)) - (a* (numpy.log(a) - 1) + numpy.e * numpy.sin(a))


a, b = 15, 50
h = 2e-1
argx = numpy.linspace(a, b, int((b - a) / h) + 1)

# first function calculations
analytics_sum_1 = sum_analytics_first(a, b)
left_sum_1 = left_sum(first_func, argx, h)
right_sum_1 = right_sum(first_func, argx, h)
center_sum_1 = center_sum(first_func, argx, h)
trapezoid_sum_1 = trapezoid_sum(first_func, argx, h)
parabolic_sum_1 = parabolic_sum(first_func, argx, h)
sums_1 = [[analytics_sum_1, "absolute sums"],
          [center_sum_1, "center sums"],
          [trapezoid_sum_1, "trapezoid sums"],
          [parabolic_sum_1, "parabolic sums"]]

# second function
analytics_sum_2 = sum_analytics_second(a, b)
left_sum_2 = left_sum(second_func, argx, h)
right_sum_2 = right_sum(second_func, argx, h)
center_sum_2 = center_sum(second_func, argx, h)
trapezoid_sum_2 = trapezoid_sum(second_func, argx, h)
parabolic_sum_2 = parabolic_sum(second_func, argx, h)
sums_2 = [[analytics_sum_2, "absolute sums"],
          [center_sum_2, "center sums"],
          [trapezoid_sum_2, "trapezoid sums"],
          [parabolic_sum_2, "parabolic sums"]]

print(f"first function:", *[f"{entry[1]}: {entry[0]}" for entry in sums_1], sep="\n")
print(f"second function:", *[f"{entry[1]}: {entry[0]}" for entry in sums_2], sep="\n")

_, axis = pyplot.subplots(1, 2, figsize=(10, 4))
for i in range(len(sums_1)):
    axis[0].plot(i, sums_1[i][0], 'o', label=sums_1[i][1], markersize=10)
axis[0].grid()
axis[0].legend()
axis[0].set(xticks=numpy.arange(0, len(sums_1)), xlabel="summation method id", ylabel="summation value", title="comparison results first function")
for i in range(len(sums_2)):
    axis[1].plot(i, sums_2[i][0], 'o', label=sums_2[i][1], markersize=10)
axis[1].grid()
axis[1].legend()
axis[1].set(xticks=numpy.arange(0, len(sums_2)), xlabel="summation method id", ylabel="summation value", title="comparison results second function")
pyplot.show()