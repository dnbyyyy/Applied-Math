import math
import matplotlib.pyplot as plt


def function(x):
    try:
        return math.log(x) * math.sin(x) * x ** 2
    except ValueError:
        return float('inf')


def golden_ratio_algorithm(left, right, eps, func):
    first_point = left + 0.382 * (right - left)
    second_point = right - 0.382 * (right - left)
    f_first_point = func(first_point)
    f_second_point = func(second_point)

    while right - left > eps:
        if f_first_point < f_second_point:
            right = second_point
            second_point = first_point
            f_second_point = f_first_point
            first_point = left + 0.382 * (right - left)
            f_first_point = func(first_point)
        else:
            left = first_point
            first_point = second_point
            f_first_point = f_second_point
            second_point = right - 0.382 * (right - left)
            f_second_point = func(second_point)

    return func((left + right) / 2)


left_boarder = 0.1
right_boarder = 10


def function(x):
    try:
        return math.log(x) * math.sin(x) * x ** 2
    except ValueError:
        return float('inf')


def golden_ratio_algorithm(left, right, eps, func):
    iterations_cnt = 0
    function_ev_cnt = 0
    segment_sizes = []  # Массив размеров рассматриваемых отрезков

    first_point = left + 0.382 * (right - left)
    second_point = right - 0.382 * (right - left)
    f_first_point = func(first_point)
    f_second_point = func(second_point)
    function_ev_cnt += 2

    min_x = None
    min_y = float('inf')

    while right - left > eps:
        if f_first_point < f_second_point:
            right = second_point
            second_point = first_point
            f_second_point = f_first_point
            first_point = left + 0.382 * (right - left)
            f_first_point = func(first_point)
            function_ev_cnt += 1
        else:
            left = first_point
            first_point = second_point
            f_first_point = f_second_point
            second_point = right - 0.382 * (right - left)
            f_second_point = func(second_point)
            function_ev_cnt += 1

        segment_delta = abs(right - left)
        segment_sizes.append(segment_delta)  # Запись размера текущего отрезка в массив
        iterations_cnt += 1

        # Обновление значения минимума функции
        if f_first_point < min_y:
            min_x = first_point
            min_y = f_first_point
        if f_second_point < min_y:
            min_x = second_point
            min_y = f_second_point

    return min_x, min_y, iterations_cnt, function_ev_cnt, segment_sizes


left_border = 0.1
right_border = 10
eps = 0.001  # accuracy

min_x, min_y, iterations, function_evaluations, segment_sizes = golden_ratio_algorithm(
    left_border, right_border, eps, function
)
print(f"Minimum: x={min_x}, y={min_y}")
print(f"Number of iterations: {iterations}")
print(f"Number of function evaluations: {function_evaluations}")

# Построение графика
plt.plot(range(1, iterations + 1), segment_sizes)
plt.xlabel('Iteration')
plt.ylabel('Segment Size')
plt.title('Segment Size vs Iteration')
plt.show()
eps = 0.001  # accuracy

result = golden_ratio_algorithm(left_boarder, right_boarder, eps, function)
