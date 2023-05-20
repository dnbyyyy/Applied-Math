import math as m
import matplotlib.pyplot as plt


def function(x):
    return m.log(x) * m.sin(x) * (x ** 2)


def brent_implementation(left_border, right_border, eps, func):
    function_calls = 0
    segments = []
    ratio = (3 - m.sqrt(5)) / 2
    x = w = v = (left_border + right_border) / 2
    f_x = f_w = f_v = func(x)
    iteration_count = 1
    d_prev = d_curr = right_border - left_border
    u_real: float

    count = 20
    while right_border - left_border > eps:
        g = d_prev
        d_prev = d_curr
        iteration_count += 1
        u_inter = find_u(x, w, v, f_x, f_w, f_v)
        if u_inter is not None and left_border + eps <= u_inter <= right_border - eps and abs(u_inter - x) < g / 2:
            u_real = u_inter
        else:
            if x < (left_border + right_border) / 2:
                u_real = x + ratio * (right_border - x)
                d_prev = right_border - x
            else:
                u_real = x - ratio * (x - left_border)
                d_prev = x - left_border

        f_u = func(u_real)
        function_calls += 1

        if f_u <= f_x:
            if u_real < x:
                right_border = x
            else:
                left_border = x
            v = w
            w = x
            x = u_real
            f_v = f_w
            f_w = f_x
        else:
            if u_real < x:
                left_border = u_real
            else:
                right_border = u_real
            if f_u < f_w or w == x:
                v = w
                w = u_real
                f_v = f_w
                f_w = f_u
            elif f_u <= f_v or v == x or v == w:
                v = u_real
                f_v = f_u
        segments.append(right_border - left_border)
    return func((left_border + right_border) / 2), iteration_count, function_calls, segments


def find_u(x, w, v, f_x, f_w, f_v):
    a = ((w - x) ** 2) * (f_w - f_v) - ((w - v) ** 2) * (f_w - f_x)
    b = (w - x) * (f_w - f_v) - (w - v) * (f_w - f_x)
    c = (w - x) * (w - v) * (v - x)
    if c == 0 or a == 0:
        return None
    u = x - 0.5 * b * a / c
    return u


minimum, iterations, function_calls, segments = brent_implementation(0.1, 10, 0.001, function)
minimum_x = (0.1 + 10) / 2
minimum_y = minimum
print(f"Minimum value: {minimum_y}")
print(f"Coordinates of the minimum: ({minimum_x}, {minimum_y})")
print(f"Iterations: {iterations}")
print(f"Function calls: {function_calls}")


# Plotting segment sizes against iteration number
plt.plot(range(1, iterations), segments)  # Adjust the range to include the final interval
plt.xlabel('Iteration')
plt.ylabel('Segment Size')
plt.title('Segment Size vs Iteration')
plt.show()

