import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости разности температуры от разности давления для T=295K') # Заголовок

x = [4.05, 3.5, 3.05, 2.45, 2] # Координата x
y = [3.006, 2.385, 1.937, 1.316, 0.894] # Координата y


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$\Delta P$, Па') # Подпись абсцисс
plt.ylabel('$\Delta T$, К') # Подпись ординат

yerr = [0.018*_y for _y in y]  # Погрешность по y
xerr = [0.05 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.125))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.125))
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.show()