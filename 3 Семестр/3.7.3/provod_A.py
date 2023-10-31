import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'Зависимость $\alpha(\omega)$ от $\sqrt{\nu}$') # Заголовок

x = [
    5, 7, 9, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38
    ] # Координата x

x = [math.sqrt(_x) for _x in x]


y = [
    -0.079024874,	-0.077589996,	-0.077589996,	-0.077087878,
    -0.076745989,	-0.076745989,	-0.075864789,	-0.075864789,
    -0.074942967,	-0.074753392,	-0.074173642,	-0.074173642,
    -0.073373535
    ] # Координата y

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.ylabel(r'$\alpha(\omega)$, $10^{-2}$ см$^{-1}$') # Подпись абсцисс
plt.xlabel(r'$\sqrt{\nu}$, МГц$^{1/2}$') # Подпись ординат

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.0005))
ax.yaxis.set_major_locator(MultipleLocator(0.001))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('provod_A')