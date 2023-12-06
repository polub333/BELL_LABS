import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'Амплитудно-частотные характеристики в безразмерных координатах') # Заголовок

x1 = [26.62,	26.67,	26.72,	26.8,	26.89,	27.06,	27.21,	27.29,	27.45,	27.55,	27.74,	28.07,	28.24] # Координата x
y1 = [2.11,	2.19,	2.3,	2.47,	2.68,	3.09,	3.41,	3.49,	3.51,	3.4,	3.09,	2.46,	2.15] # Координата y

x2 = [20.04,	20.12,	20.31,	20.41,	20.51,	20.7,	20.85,	21.14,	21.25,	21.36,	21.47,	21.57,	21.8,	22.04]
y2 = [1.4,	1.5,	1.75,	1.92,	2.09,	2.5,	2.74,	2.8,	2.67,	2.5,	2.31,	2.15,	1.79,	1.48]

x1 = [x / 27.3 for x in x1]
y1 = [y / 3.55 for y in y1]

x2 = [x / 21.06 for x in x2]
y2 = [y / 2.87 for y in y2]

plt.scatter(x1, y1, s=18, c='green')  # Экспериментальные точки на графике.
plt.scatter(x2, y2, s=18, c='red')  # Экспериментальные точки на графике

plt.xlabel(r'$\frac{f}{f_0}$') # Подпись абсцисс
plt.ylabel(r'$\frac{U_C}{U_{C_0}}$') # Подпись ординат

line1, = plt.plot(x1, y1, label='25 нФ', c='green')
line2, = plt.plot(x2, y2, label='57.2 нФ', c='red')

DP = 2
ax = plt.gca()
ax.legend(handles=[line1, line2])

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.01))
ax.yaxis.set_major_locator(MultipleLocator(0.04))
ax.xaxis.set_minor_locator(MultipleLocator(0.0025))
ax.xaxis.set_major_locator(MultipleLocator(0.01))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('a_ch_h_2')