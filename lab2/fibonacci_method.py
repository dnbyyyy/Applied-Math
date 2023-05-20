import math
import matplotlib.pyplot as plt


def function(x):
    return math.log(x) * math.sin(x) * x ** 2


def preset_values(a, b, eps):
    n = find_n((b - a) / eps)

    length = (b - a) / find_fib_on(n)
    x_1 = a + length * find_fib_on(n - 2)
    x_2 = b - length * find_fib_on(n - 2)

    return n, length, x_1, x_2


def complement(total_iterations, cur_iterations, localization_segment):
    return localization_segment * find_fib_on(total_iterations - cur_iterations - 1)


def find_fib_on(position):
    if position <= 1:
        return position
    else:
        return find_fib_on(position - 1) + find_fib_on(position - 2)


def find_n(number):
    prev_1 = 1
    prev_2 = 1
    num_fib = 0
    count = 0
    while num_fib <= number:
        num_fib = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = num_fib
        count += 1

    return count


def fibonacci_method(function, left_boarder, right_boarder, eps):
    start_interval = left_boarder
    end_interval = right_boarder
    n, length, x_1, x_2 = preset_values(left_boarder, right_boarder, eps)
    iterations_count = 1
    function_usage_count = 2
    f_x1 = function(x_1)
    f_x2 = function(x_2)
    segment_delta_array = [right_boarder - left_boarder]

    while iterations_count != n:
        iterations_count += 1
        if f_x1 < f_x2:
            end_interval = x_2
            x_2 = x_1
            f_x2 = f_x1
            x_1 = start_interval + complement(n, iterations_count, length)
            f_x1 = function(x_1)
        else:
            start_interval = x_1
            x_1 = x_2
            f_x1 = f_x2
            x_2 = end_interval - complement(n, iterations_count, length)
            f_x2 = function(x_2)

        segment_delta = abs(end_interval - start_interval)
        segment_delta_array.append(segment_delta)
        function_usage_count += 1

    x_minimum = (x_1 + x_2) / 2
    y_minimum = function(x_minimum)

    return x_minimum, y_minimum, iterations_count, function_usage_count, segment_delta_array


minimum_x, minimum_y, iterations_count, function_usage_count, segment_delta_array = fibonacci_method(function, 0.1, 10, 1e-6)

print(f"Minimum: x={minimum_x:.6f}, y={minimum_y:.6f}")
print(f"Iterations: {iterations_count}")
print(f"Function evaluations: {function_usage_count}")

# Построение графика
plt.plot(range(1, iterations_count + 1), segment_delta_array)
plt.xlabel('Iteration')
plt.ylabel('Segment Size')
plt.title('Segment Size vs Iteration')
plt.show()
