from math import log, sin
import matplotlib.pyplot as plt


def function(x):
    return log(x) * sin(x) * x ** 2


def dichotomy_implementation(left, right, eps):
    iterations_cnt = 0
    function_ev_cnt = 0
    segment_sizes = []  # Массив размеров рассматриваемых отрезков

    while (right - left) > eps:
        c = (left + right) / 2
        x1 = (left + c) / 2
        x2 = (c + right) / 2

        f_x1 = function(x1)
        f_x2 = function(x2)
        function_ev_cnt += 2

        if f_x1 < f_x2:
            right = x2
        else:
            left = x1

        iterations_cnt += 1
        segment_sizes.append(right - left)  # Запись размера текущего отрезка в массив

    return (left + right) / 2, iterations_cnt, function_ev_cnt, segment_sizes


left_boarder = 0.1
right_boarder = 10
eps = 0.001

left_boarder, right_boarder = min(left_boarder, right_boarder), max(left_boarder, right_boarder)

minimum, iterations, function_evaluations, segment_sizes = dichotomy_implementation(left_boarder, right_boarder, eps)

print(f"func minimum on the [{left_boarder}, {right_boarder}] equals {minimum} with {function(minimum)} func value")
print(f"Number of iterations: {iterations}")
print(f"Number of function evaluations: {function_evaluations}")

# Построение графика
plt.plot(range(1, iterations + 1), segment_sizes)
plt.xlabel('Iteration')
plt.ylabel('Segment Size')
plt.title('Segment Size vs Iteration')
plt.show()
