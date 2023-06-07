import numpy as np
import matplotlib.pyplot as plt


def brent(eps, f, a, b):
    segments = []
    count_iter, count_func = 0, 0

    phi = (3 - np.sqrt(5)) / 2
    x = w = v = a + phi * (b - a)
    fx = fw = fv = f(x)
    d, e = b - a, b - a

    while d > eps:
        g = e
        e = d

        u = None
        if x != w and x != v and w != v and fx != fw and fx != fv and fw != fv:
            p = (x - w) * (fx - fv) - (x - v) * (fx - fw)
            q = 2 * (x - w) * (fx - fv) - 2 * (x - v) * (fx - fw)

            if q != 0:
                u = x - (p / q)
                if a + eps <= u <= b - eps and np.abs(u - x) < g / 2:
                    d = np.abs(u - x)
                else:
                    u = None

        if u is None:
            if x < (b + a) / 2:
                u = x + phi * (b - x)
                d = b - x
            else:
                u = x - phi * (x - a)
                d = x - a

            if np.abs(u - x) < eps:
                u = x + np.sign(u - x) * eps

        fu = f(u)
        count_func += 1

        if fu <= fx:
            if u >= x:
                a = x
            else:
                b = x

            v, w, x = w, x, u
            fv, fw, fx = fw, fx, fu
        else:
            if u >= x:
                b = u
            else:
                a = u

            if fu <= fw or w == x:
                v, w = w, u
                fv, fw = fw, fu
            elif fu <= fv or v == x:
                v, fv = u, fu

        segments.append(b - a)
        count_iter += 1

        if d < eps:  # Выход из алгоритма при достижении размера интервала меньше eps
            break

    return x, count_iter, count_func, segments


def function(x):
    return np.log(x) * np.sin(x) * (x ** 2)


def multimodal(x):
    return (x ** 4) - (4 * (x ** 3)) + (4 * (x ** 2))


x_min, iterations, function_calls, ratios = brent(0.0001, multimodal, -2, 4)
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
