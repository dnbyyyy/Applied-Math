from math import log, sin
import matplotlib.pyplot as plt


def function(x):
    return log(x) * sin(x) * x ** 2


def multimodal(x):
    return x ** 4 - 4 * x ** 3 + 4 * x ** 2


def dichotomy(eps, f, a, b):
    iterations_cnt = 0
    function_ev_cnt = 0
    segment_sizes = []  # Массив размеров рассматриваемых отрезков

    while (b - a) > eps:
        c = (a + b) / 2
        x1 = (a + c) / 2
        x2 = (c + b) / 2

        f_x1 = f(x1)
        f_x2 = f(x2)
        function_ev_cnt += 2

        if f_x1 < f_x2:
            b = x2
        else:
            a = x1

        iterations_cnt += 1
        segment_sizes.append(b - a)  # Запись размера текущего отрезка в массив

    return (a + b) / 2, iterations_cnt, function_ev_cnt, segment_sizes


left_boarder = -2
right_boarder = 4
eps = 0.0001

minimum, iterations, function_evaluations, segment_sizes = dichotomy(eps, multimodal, left_boarder, right_boarder)

print(f"Минимум функции на интервале [{left_boarder}, {right_boarder}] равен {minimum} с функциональным значением {multimodal(minimum)}")
print(f"Количество итераций: {iterations}")
print(f"Количество вычислений функции: {function_evaluations}")

# Построение графика
plt.plot(range(1, iterations + 1), segment_sizes)
plt.xlabel('Итерация')
plt.ylabel('Размер интервала')
plt.title('Зависимость размера интервала от итерации')
plt.show()
