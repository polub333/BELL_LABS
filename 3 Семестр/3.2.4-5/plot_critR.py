import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math as math

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'График зависимости $\frac{1}{\theta^2}$ от $\frac{1}{(R_\sum)^2}$') # Заголовок

y = [0.355, 0.53, 0.74, 0.92, 0.91, 0.95, 1.30, 1.80] # Координата x
x = [460, 687, 952, 1178, 1165, 1219, 1660, 2250] # Координата y

x = [1/(_x*_x)*1000000 for _x in x]
y = [1/(_y*_y) for _y in y]


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$\frac{1}{(R_\sum)^2}$, $10^{-6}~Ом ^{-1}$') # Подпись абсцисс
plt.ylabel(r'$\frac{1}{\theta^2}$') # Подпись ординат


'''plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')'''

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot_critR')