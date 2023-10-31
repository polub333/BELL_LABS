import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'Зависимость $\alpha(\omega)*k(\omega)$ от $\nu^{3/2}$') # Заголовок

x = [
    5, 7, 9, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38
    ] # Координата x

x = [_x*math.sqrt(_x) for _x in x]


y = [
    -0.002730904,	-0.007644193,	-0.012899576,	-0.017582174,
    -0.02463125,	-0.032076561,	-0.038705809,	-0.046027499,
    -0.052361917,	-0.059500255,	-0.066230834,	-0.073411682,
    -0.078377006
    ] # Координата y

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.ylabel(r'$\alpha(\omega)*k(\omega)$, $10^{-4}$ см$^{-2}$') # Подпись абсцисс
plt.xlabel(r'$\nu^{3/2}$, МГц$^{3/2}$') # Подпись ординат

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(0.01))
ax.xaxis.set_minor_locator(MultipleLocator(10))
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('provod_B')