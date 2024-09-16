import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График количества частиц в секунду от тока, протекающего через катушку') # Заголовок

y = [1.424,
1.562,
1.737,
1.887,
1.887,
1.662,
2.361,
2.924,
3.336,
3.261,
3.561,
3.898,
3.873,
3.149,
3.124,
2.561,
2.624,
3.149,
3.236,
4.111,
3.498,
3.511,
2.686,
2.212,
1.287,
0.862,
0.825
] # Координата x
x = [0,
0.2,
0.4,
0.6,
0.8,
1,
1.2,
1.4,
1.6,
1.8,
2,
2.2,
2.4,
2.6,
2.8,
3,
3.2,
3.4,
3.5,
3.6,
3.7,
3.8,
3.9,
4,
4.2,
4.4,
4.46
] # Координата y


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$I$, А') # Подпись абсцисс
plt.ylabel('$N$, с$^{-1}$') # Подпись ординат

yerr = [0 for _y in y]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

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

plt.savefig('raw.png')