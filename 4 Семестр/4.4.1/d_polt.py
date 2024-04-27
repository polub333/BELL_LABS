import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def foo(deg, min, sec):
    return deg + min/60 + sec / 3600

center = 181*3600 + 39

plt.figure(figsize=(10,7))  #Размер изображения

x = [-2, -1, 0, 1, 2] # Координата x
y = [foo(216, 15, 31) - foo(215, 65, 39), foo(197, 56, 21) - foo(197, 52, 48), 0, foo(164, 14, 44) - foo(164, 13, 59), foo(145, 43, 3) - foo(145, 32, 56)] # Координата y
y = [_y *3600 / 21 for _y in y]

print(y)

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('m') # Подпись абсцисс
plt.ylabel(r'$D$, угл. секунда/ $\AA$') # Подпись ординат

#yerr = [0.018*_y for _y in y]  # Погрешность по y
#xerr = [0.05 for _x in x] # Погрешность по x
#plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

def f(x):
    return np.abs(x) / np.sqrt((2.74185 * 10000)**2 - x**2 *3.8* (578.05*10)**2) * 206264

xx = np.arange(-2, 2, 0.01)
plt.plot(xx, f(xx))

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('d_plot')