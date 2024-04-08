import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости длины волны от частоты генератора') # Заголовок

x = [1.036, 2.873, 1.270, 5.218] # Координата x
x = [1/_x for _x in x]
y = [1.613, 0.578, 1.263, 0.324] # Координата y

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$\frac{1}{\nu}$, $10^{-6}$ с') # Подпись абсцисс
plt.ylabel('$\Lambda$, мм') # Подпись ординат

#yerr = [0.018*_y for _y in y]  # Погрешность по y
#xerr = [0.05 for _x in x] # Погрешность по x
#plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('v_1')