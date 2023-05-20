from math import sin, log
import matplotlib.pyplot as plt


def function(x):
    return log(x) * sin(x) * (x ** 2)


def parabola_implementation(left_boarder, right_boarder, eps):
    iteration = 0
    calls = 0
    segments = []

    while right_boarder - left_boarder > eps:
        middle = (left_boarder + right_boarder) / 2
        f_l = function(left_boarder)
        f_m = function(middle)
        f_r = function(right_boarder)

        calls += 3

        u = abs(middle - (((middle - left_boarder) ** 2) * ((f_m - f_r) - ((middle - right_boarder) ** 2) * (f_r - f_l))
                          / (2 * ((middle - left_boarder) * (f_m - f_r) - (middle - right_boarder) * (f_m - f_l)))))

        f_u = function(u)
        calls += 1

        if middle < u:
            if f_m > f_u:
                left_boarder = u
            else:
                right_boarder = middle

        if middle >= u:
            if f_m > f_u:
                right_boarder = u
            else:
                left_boarder = middle

        iteration += 1
        segments.append(right_boarder - left_boarder)

    return u, f_u, iteration, calls, segments


minimum_x, minimum_y, iterations_count, function_usage_count, segment_delta_array = parabola_implementation(0.1, 10, 0.001)

print(f"Minimum: x={minimum_x:.6f}, y={minimum_y:.6f}")
print(f"Iterations: {iterations_count}")
print(f"Function evaluations: {function_usage_count}")

# Построение графика
plt.plot(range(1, iterations_count + 1), segment_delta_array)
plt.xlabel('Iteration')
plt.ylabel('Segment Size')
plt.title('Segment Size vs Iteration')
plt.show()
