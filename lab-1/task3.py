import numpy

# import methods from first task
from differentiation import right_diff, left_diff, diff
from task2 import first_func, second_func, first_func_derivative, second_func_derivative

a, b = 15, 50
h = 2e-1
argx = numpy.linspace(a, b, int((b - a) / h) + 1)

# analytic counts
analytic_diff_first = first_func_derivative(argx)
analytic_diff_second = second_func_derivative(argx)

# first function
right_diff_first = right_diff(first_func, argx, h)
left_diff_first = left_diff(first_func, argx, h)
diff_first = diff(first_func, argx, h)

# second function
right_diff_second = right_diff(second_func, argx, h)
left_diff_second = left_diff(second_func, argx, h)
diff_second = diff(second_func, argx, h)

# first mse
mse_left_first = sum((x - a) ** 2 for x, a in zip(left_diff_first, analytic_diff_first)) / len(analytic_diff_first)
mse_right_first = sum((x - a) ** 2 for x, a in zip(right_diff_first, analytic_diff_first)) / len(analytic_diff_first)
mse_center_first = sum((x - a) ** 2 for x, a in zip(diff_first, analytic_diff_first)) / len(analytic_diff_first)

# second mse
mse_left_second = sum((x - a) ** 2 for x, a in zip(left_diff_second, analytic_diff_second)) / len(analytic_diff_second)
mse_right_second = sum((x - a) ** 2 for x, a in zip(right_diff_second, analytic_diff_second)) / len(analytic_diff_second)
mse_center_second = sum((x - a) ** 2 for x, a in zip(diff_second, analytic_diff_second)) / len(analytic_diff_second)
print(
    f"for the first function\nleft derivatives mse are: {mse_left_first}\nright derivatives mse are: {mse_right_first}\ncenter derivatives mse are: {mse_center_first}")
print(
    f"for the second function\nleft derivatives mse are: {mse_left_second}\nright derivatives mse are: {mse_right_second}\ncenter derivatives mse are: {mse_center_second}")
