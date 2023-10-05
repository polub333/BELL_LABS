import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math as math

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'График зависимости $\Delta \phi$ от $\omega$') # Заголовок

y1 = [-1.788, -1.772, -1.756, -1.745, -1.720, -1.704, -1.682,
      -1.663, -1.621, -1.604, -1.570, -1.540] # Координата x
x1 = [3.8, 4, 4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25, 6.5] # Координата y

x2 = [5.3, 5.37, 5.44, 5.51, 5.58, 5.65, 5.72, 5.79, 5.86, 5.93, 6,
      6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7]
y2 = [-1.774, -1.770, -1.76, -1.742, -1.733, -1.717, -1.685, -1.651, -1.638,
      -1.601, -1.57, -1.536, -1.488, -1.449, -1.432, -1.412, -1.396, -1.377,
      -1.361, -1.348, -1.335]

#x = [0, 942, 1115, 1185, 1409, 1490, 1595, 1659, 1775, 1805, 1869, 1938]
#plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$\omega$') # Подпись абсцисс
plt.ylabel(r'$\Delta \phi$') # Подпись ординат


'''plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)
'''

line1, = plt.plot(x1, y1, label='2000 Ом', c='red')
line2, = plt.plot(x2, y2, label='408 Ом', c='green')


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.legend(handles=[line1, line2])

ax.yaxis.set_minor_locator(MultipleLocator(3.1415/100))
ax.yaxis.set_major_locator(MultipleLocator(3.1415/50))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot_fch')