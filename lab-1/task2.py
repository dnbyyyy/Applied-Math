from matplotlib import pyplot
import numpy
# import methods from first task
from differentiation import right_diff, left_diff, diff


def first_func(x):
    return numpy.log(x) * numpy.sin(x)


def second_func(x):
    return numpy.e ** (numpy.cos(x) * numpy.log(x))


def first_func_derivative(x):
    return numpy.sin(x) / x + numpy.log(x) * numpy.cos(x)


def second_func_derivative(x):
    return x ** (numpy.cos(x) - 1) * (numpy.cos(x) - x * numpy.log(x) * numpy.sin(x))


a, b = 15, 50
h = 2e-1
argx = numpy.linspace(a, b, int((b - a) / h) + 1)

# graphs
_, axis = pyplot.subplots(1, 2, figsize=(10, 4))
axis[0].plot(argx, first_func(argx))
axis[1].plot(argx, second_func(argx))
axis[0].grid()
axis[1].grid()
axis[0].set(title=f'Graph of first function', xlabel='$x$', ylabel="$f(x)$")
axis[1].set(title=f'Graph of second function', xlabel='$x$', ylabel="$f(x)$")
pyplot.show()

# analytic counts
analytic_diff_first = first_func_derivative(argx)
analytic_diff_second = second_func_derivative(argx)

_, axis_analytic = pyplot.subplots(1, 2, figsize=(10, 4))
axis_analytic[0].plot(argx, analytic_diff_first, 'o-', linewidth=2)
axis_analytic[1].plot(argx, analytic_diff_second, 'o-', linewidth=2)
axis_analytic[0].grid()
axis_analytic[1].grid()
axis_analytic[0].set(title='Derivative for first function', xlabel='$x$', ylabel="$f $'$(x)$")
axis_analytic[1].set(title='Derivative for second function', xlabel='$x$', ylabel="$f $'$(x)$")
pyplot.show()

# first function
right_diff_first = right_diff(first_func, argx, h)
left_diff_first = left_diff(first_func, argx, h)
diff_first = diff(first_func, argx, h)

# second function
right_diff_second = right_diff(second_func, argx, h)
left_diff_second = left_diff(second_func, argx, h)
diff_second = diff(second_func, argx, h)


def plot_compare(func: str, derivative_pairs, arguments, h):
    _, ax = pyplot.subplots(1, 1, figsize=(12, 8))
    for i in range(len(derivative_pairs)):
        ax.scatter(arguments, derivative_pairs[i][0], label=f"{derivative_pairs[i][1]} method", s=50)
    ax.grid()
    ax.legend()
    ax.set(title=f'Comparison of derivative values with step $h={h}$ for {func} function',
           xlabel='$x$', ylabel="$y'(x)$")
    pyplot.show()


plot_compare("First", [[right_diff_first[-3:], "right"],
                       [left_diff_first[-3:], "left"],
                       [diff_first[-3:], "center"],
                       [analytic_diff_first[-3:], "analytic"]], argx[-3:], h)
plot_compare("Second", [[right_diff_second[-3:], "right"],
                        [left_diff_second[-3:], "left"],
                        [diff_second[-3:], "center"],
                        [analytic_diff_second[-3:], "analytic"]], argx[-3:], h)
