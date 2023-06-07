import math
import matplotlib.pyplot as plt
import numpy as np

def gen_fib(min_fib):
    fib_seq = [1, 1]
    while fib_seq[-1] <= min_fib:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def fibonacci(eps, func, a, b):
    count_iter, count_func, prev_len = 1, 2, b - a
    segment_sizes, arr_b, arr_ratio = [a], [b], []
    fib_seq = gen_fib(math.ceil((b - a) / eps))
    n = len(fib_seq) - 1
    if n < 2:
        x1, x2 = a, b
    else:
        x1, x2 = a + fib_seq[n - 2] / fib_seq[n] * (b - a), a + fib_seq[n - 1] / fib_seq[n] * (b - a)
    f1, f2 = func(x1), func(x2)
    k = 1
    while k + 2 < n:
        if f1 > f2:
            a = x1
            if n - k < 2:
                x1 = a
            else:
                x1 = a + fib_seq[n - k - 2] / fib_seq[n - k] * (b - a)
            x2 = a + fib_seq[n - k - 1] / fib_seq[n - k] * (b - a)
            f1, f2 = f2, func(x2)
        else:
            b = x2
            x1 = a + fib_seq[n - k - 2] / fib_seq[n - k] * (b - a)
            if n - k < 1:
                x2 = b
            else:
                x2 = a + fib_seq[n - k - 1] / fib_seq[n - k] * (b - a)
            f1, f2 = func(x1), f1
        segment_sizes.append(b - a)
        count_iter += 1
        count_func += 1
        k += 1
    return (a + b) / 2, count_iter, count_func, segment_sizes


def function(x):
    return np.log(x) * np.sin(x) * (x ** 2)


def multimodal(x):
    return x ** 4 - 4 * x ** 3 + 4 * x ** 2


x_min, iterations, function_calls, ratios = fibonacci(0.0001, multimodal, -2, 4)
f_min = multimodal(x_min)

print("Минимум функции:", x_min)
print("Значение функции в минимуме:", f_min)
print("Количество итераций:", iterations)
print("Количество вычислений функции:", function_calls)


plt.plot(range(1, iterations), ratios[1:])
plt.xlabel("Номер итерации")
plt.ylabel("Размер интервала")
plt.title("Зависимость размера интервала от номера итерации")
plt.show()
