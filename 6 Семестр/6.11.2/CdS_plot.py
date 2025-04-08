import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения

x = [4600,
4700,
4820,
4950,
5100,
5220,
5370,
5500,
5680,
5870,
6090,
6340,
6470,
6620,
6780,
6940,
7330,
7800,
8080,
8330,
8600,
8900,
9140,
9400,
9980,
] # Координата x
y = [3.30,
2.89,
1.90,
1.53,
2.03,
5.81,
5.31,
4.70,
4.34,
4.24,
4.29,
4.40,
4.58,
4.72,
4.84,
4.78,
4.67,
4.16,
3.73,
2.95,
2.00,
1.20,
0.74,
0.37,
0.05,
] # Координата y


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$\lambda$, $\AA$') # Подпись абсцисс
plt.ylabel(r'$U$, мВ') # Подпись ординат

yerr = [0.1 for _y in y]  # Погрешность по y
xerr = [50 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.25))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(250))
ax.xaxis.set_major_locator(MultipleLocator(500))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('CdS_plot')