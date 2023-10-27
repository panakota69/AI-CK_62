import numpy as np
from random import randint

# Задание 1
# Создание вектора сост. из чисел от 1 до 25
vec = np.arange(1, 26)
# Преобразование в матрицу 5*5
vec1 = np.arange(1, 26).reshape(5, 5)
print(f'Матрица задание 1 \n {vec1}')

# Задание 2
# Создаем массив с рандомными числами в диапозоне от -5 до 100
mass = [randint(-5, 100) for _ in range(30)]
# Массив в вектор=>матрица
matr = np.array(mass).reshape(5, 6)
print(f'Матрица задания 2 исходная \n {matr}')
x = np.argmax(mass)
y = np.argmin(mass)
mass[x] = -5
mass[y] = 100
matr = np.array(mass).reshape(5, 6)
print(f'Матрица задания 2 преобразованная\n {matr}')
