import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'Фазово-частотные характеристики в безразмерных координатах') # Заголовок

x1 = [25.51,	25.77,	26,	26.2,	26.55,	26.85,	27.09,	27.39,	27.85,	28.14,	28.55,	28.96] # Координата x
y1 = [0.075,	0.102564103,	0.115789474,	0.131578947,	0.168421053,	0.238095238,	0.344086022,	0.5,	0.694444444,	0.75,	0.823863636,	0.857142857]

x2 = [18.97,	19.26,	19.56,	19.86,	20.14,	20.58,	20.98,	21.27,	21.51,	21.86,	22.23,	22.5,	22.87]
y2 = [0.057251908,	0.076923077,	0.08627451,	0.12,	0.16,	0.272727273,	0.466666667,	0.617021277,	0.711206897,	0.782608696,	0.844444444,	0.864864865,	0.890909091]

x1 = [x / 27.3 for x in x1]
x2 = [x / 21.06 for x in x2]

plt.scatter(x1, y1, s=18, c='green')  # Экспериментальные точки на графике.
plt.scatter(x2, y2, s=18, c='red')  # Экспериментальные точки на графике

plt.xlabel(r'$\frac{f}{f_0}$') # Подпись абсцисс
plt.ylabel(r'$\frac{\phi_C}{\pi}$, В') # Подпись ординат

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

plt.savefig('f_ch_h')