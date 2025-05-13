import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения

x = [0,
0.0016,
0.0022,
0.0035,
0.0048,
0.0062,
0.01,
0.02,
0.026,
0.028,
0.03,
0.0319,
0.04,
0.232,
0.228,
0.322,
0.343,
0.39,
0.398,
0.411,
0.433,
0.454,
0.461,
0.4907,
0.4921,
] # Координата x
y = [0,
0.255,
0.376,
0.616,
0.852,
1.074,
1.696,
3.061,
3.616,
3.72,
3.93,
3.995,
4.07,
2.148,
2.101,
1.03,
0.887,
0.5,
0.551,
0.639,
0.894,
1.335,
1.595,
3.49,
3.665,
] # Координата y


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$U$, В') # Подпись абсцисс
plt.ylabel('$I$, мА') # Подпись ординат

yerr = [0.018*_y for _y in y]  # Погрешность по y
xerr = [0.05 for _x in x] # Погрешность по x
#plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

#p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
#p_f = np.poly1d(p)
#plt.plot(x, p_f(x))
#print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.01))
ax.xaxis.set_major_locator(MultipleLocator(0.05))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot')