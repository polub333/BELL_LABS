import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения

x = [4600,
4820,
5100,
5370,
5680,
6090,
6620,
6940,
7140,
7200,
7300,
7330,
7380,
7420,
7460,
7520,
7560,
7640,
7900,
8330,
8900,
9140,
9300,
9400,
9520,
9560,
9640,
9700,
9810,
9980,
] # Координата x
y = [0.40,
0.33,
0.23,
0.21,
0.22,
0.29,
0.48,
0.66,
1.08,
1.66,
2.24,
2.72,
3.37,
3.77,
3.97,
4.34,
4.61,
4.84,
4.88,
4.50,
4.12,
3.67,
3.13,
2.69,
2.20,
1.90,
1.64,
1.43,
1.04,
0.60,
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

plt.savefig('CdSe_plot')