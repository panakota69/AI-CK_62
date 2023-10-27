import math as m
import numpy as np
import matplotlib.pyplot as plt


x_1 = (m.pi/3)
function_x = (m.sin(0.8*x_1) + m.cos(-2.4*x_1))/2*x_1
print(f'Значение функции в точке x1 = {function_x}')
vector_x = np.arange(start=-2*m.pi, stop=4*m.pi+1, step=m.pi/30, dtype=float)
print(f'Вектор x от -2п до 4п с шагом п/30:\n {vector_x}')
print(f'Точек на графике = {len(vector_x)}')
for i in range(len(vector_x)):
    y_1 = (m.sin(0.8*vector_x[i]) + m.cos(-2.4*vector_x[i]))/2*vector_x[i]
    print(y_1)


def funct_y(x, a=1):
    y = (m.sin(0.8*x) + m.cos(-2.4*x))/2*x
    return y


x_start = 2*m.pi
x_end = 4*m.pi
dx = m.pi/30
d_range = round((x_end - x_start)/dx) + 1
x = []
yy = []
for i in range(d_range):
    x.append(x_start)
    yy.append(funct_y(x_start))
    x_start = x_start + dx

plt.plot(x, yy)
plt.title("График зависимости y(x)")
plt.xlabel("x")
plt.ylabel("y(x)")
