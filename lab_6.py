import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt


# 1
def f(x):
    return x**3/(x**8-2)


# Определяем точное решение интеграла
def exact_solution():
    return -np.log(np.sqrt(2))


# Вычисляем интеграл численно
result, error = integrate.quad(f, 0.0, 1.0)
# Выводим результаты
print(f'Численное решение: {result}')
print(f'Точное решение: {exact_solution()}')
print(f'Абсолютная погрешность: {abs(result - exact_solution())}')


# 2
def diff_eqn(y, x):
    return (1/np.sin(x)**3) - y


x_0 = np.pi/4
y_0 = 2
dydx0 = 1

x = np.linspace(x_0, 2*np.pi, 100)

# Численное решение
sol = integrate.odeint(diff_eqn, [y_0, dydx0], x)
y_numerical = sol[:, 0]


# Точное решение
def exact_solution(x):
    return (3*np.sin(x) + np.cos(x))/(3*np.cos(x)-np.sin(x))


y_exact = exact_solution(x)

# Относительная ошибка
rel_error = np.abs(y_exact - y_numerical) / np.abs(y_exact)

# Графики
plt.figure(figsize=(10, 6))
plt.plot(x, y_numerical, label='Численное решение')
plt.plot(x, y_exact, label='Точное решение')
plt.plot(x, rel_error, label='Относительная ошибка')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()
