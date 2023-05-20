import numpy as np
import matplotlib.pyplot as plt

# задаем область определения
dx = np.linspace(0.1, 10, 1000)

# вычисляем значения функции на заданной области определения
dy = np.log(dx) * np.sin(dx) * dx ** 2

plt.plot(dx, dy)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y(x) = ln(x) * sin(x) * x^2')
plt.show()
