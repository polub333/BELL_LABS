import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения

x1 = [
    0,
-4.52,
-4.2,
-3.84,
-3.5,
-3.15,
-2.77,
-2.41,
-1.98,
-1.75,
-1.5,
-1.52,
-1.35,
-1.13,
-0.78,
0,
4.51,
4.22,
3.87,
3.53,
3.17,
2.79,
2.45,
2,
1.78,
1.54,
1.52,
1.36,
1.14,
0.79
] # Координата x
y1 = [
    1488.6,
1477.9,
1486.9,
1490.4,
1495.5,
1488.9,
1466.6,
1483.9,
1462.3,
1483.4,
1463.6,
1478.9,
1475.7,
1472.5,
1477.1,
1488.6,
1466,
1450,
1453.1,
1445.6,
1415.4,
1373.2,
1336.7,
1338.5,
1394.5,
1436,
1435.8,
1450.1,
1485.7,
1480.8
] # Координата y



plt.scatter(x1, y1, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$v$, мм/с') # Подпись абсцисс
plt.ylabel('$I$, с$^{-1}$') # Подпись ординат

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_minor_locator(MultipleLocator(0.25))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot1')