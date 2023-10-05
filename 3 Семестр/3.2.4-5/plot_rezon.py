import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math as math

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'График зависимости $\frac{U}{U_0}$ от $\frac{\nu}{\nu_0}$') # Заголовок

y1 = [0.894, 1, 0.986, 0.944, 0.970, 0.792, 0.714, 0.635, 0.552, 0.460, 0.400, 0.359] # Координата x
x1= [1.04, 1, 0.96, 0.92, 0.88, 0.84, 0.8, 0.76, 0.72, 0.68, 0.64, 0.608] # Координата y

x2 = [1.16, 1.15, 1.13, 1.11, 1.1, 1.08, 1.06, 1.05, 1.03, 1.01,
      1, 0.988, 0.976, 0.965, 0.953, 0.941, 0.93, 0.918, 0.906, 0.895, 0.883]
y2 = [0.413, 0.441, 0.470, 0.523, 0.558, 0.610, 0.697, 0.790, 0.860, 0.930,
      1, 0.947, 0.901, 0.848, 0.773, 0.674, 0.598, 0.540, 0.470, 0.430, 0.401]

#x = [0, 942, 1115, 1185, 1409, 1490, 1595, 1659, 1775, 1805, 1869, 1938]

#plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$\frac{U}{U_0}$') # Подпись абсцисс
plt.ylabel(r'$\frac{\nu}{\nu_0}$') # Подпись ординат


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

ax.yaxis.set_minor_locator(MultipleLocator(0.025))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.01))
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot_rezon')