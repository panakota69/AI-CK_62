import math as m
import numpy as np
import matplotlib.pyplot as plt


fsize = 12
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'

# массив координат – 50 точек в диапазоне [0,10 ]
x = np.linspace(0.0, 10.0, 50)
# создаём окно рисунка.
fig = plt.figure()
# 3*3, т.к при использовании 2*2 пропадают
ax1 = fig.add_subplot(3, 3, 1)
# верхние подписи осей, а боковые съезжают

ax1.plot(x, np.sin(x), 'k-')
ax1.set_title('(а)')

ax2 = fig.add_subplot(3, 3, 3)
ax2.plot(x, np.cos(x), 'k:')
ax2.set_title('(б)')

ax3 = fig.add_subplot(3, 3, 7)
ax3.plot(x, (np.cos(x))**2.0, 'k--')
ax3.set_title('(в)')

ax4 = fig.add_subplot(3, 3, 9)
ax4.plot(x, (x)**0.15, '-', color='gray')
ax4.set_title('(г)')

# диапазон отображаемых значений по оси х
ax1.set_xlim(0, 2*m.pi)
ax2.set_xlim(0, 2*m.pi)
ax3.set_xlim(0, 2*m.pi)
ax4.set_xlim(0, 2*m.pi)
# диапазон отображаемых значений по оси yax.set_ylim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax3.set_ylim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)
# подпись по оси x
ax1.set_xlabel(r'$x$')
ax2.set_xlabel(r'$x$')
ax3.set_xlabel(r'$x$')
ax4.set_xlabel(r'$x$')
# подпись по оси y
ax1.set_ylabel(r'$f(x)$')
ax2.set_ylabel(r'$f(x)$')
ax3.set_ylabel(r'$f(x)$')
ax4.set_ylabel(r'$f(x)$')
fig.savefig("relust_lab_3.png", orientation='landscape', dpi=300)
