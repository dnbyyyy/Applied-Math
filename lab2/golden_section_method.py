import matplotlib.pyplot as plt
import numpy as np


def golden_section(eps, func, a, b):
    golden_const_1 = ((-5 ** 0.5 + 3) / 2)
    golden_const_2 = 1 / ((5 ** 0.5 + 1) / 2)
    count_iter, count_func = 0, 0
    segments = []
    saved_part = 0
    prev_func = None
    while b - a > eps:
        x1, x2 = a + golden_const_1 * (b - a), a + golden_const_2 * (b - a)
        if saved_part == 0:
            f_x1, f_x2 = func(x1), func(x2)
            count_func += 2
        elif saved_part == -1:
            f_x1, f_x2 = prev_func, func(x2)
            count_func += 1
        else:
            f_x1, f_x2 = func(x1), prev_func
            count_func += 1
        if f_x1 < f_x2:
            b = x2
            saved_part = 1
            prev_func = f_x1
        elif f_x1 > f_x2:
            a = x1
            saved_part = -1
            prev_func = f_x2
        else:
            a, b = x1, x2
            saved_part = 0
        count_iter += 1
        segments.append(b - a)

    return (a + b) / 2, count_iter, count_func, segments


def function(x):
    return np.log(x) * np.sin(x) * (x ** 2)


def multimodal(x):
    return x ** 4 - 4 * x ** 3 + 4 * x ** 2


x_min, iterations, function_calls, ratios = golden_section(0.0001, multimodal, -2, 4)
f_min = multimodal(x_min)

print("Минимум функции:", x_min)
print("Значение функции в минимуме:", f_min)
print("Количество итераций:", iterations)
print("Количество вычислений функции:", function_calls)

plt.plot(range(1, iterations + 1), ratios)
plt.xlabel("Номер итерации")
plt.ylabel("Размер интервала")
plt.title("Зависимость размера интервала от номера итерации")
plt.show()
