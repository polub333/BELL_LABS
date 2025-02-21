import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения

x = [
    0,
-4.87,
-4.51,
-4.16,
-3.81,
-3.5,
-3.16,
-2.79,
-2.42,
-1.98,
-1.5,
-1.51,
-1.36,
-1.05,
-0.77,
0,
4.89,
4.54,
4.18,
3.84,
3.51,
3.17,
2.82,
2.45,
2.01,
1.54,
1.52,
1.37,
1.05,
0.78
] # Координата x
y = [
    297.5,
284.1,
287.5,
290.9,
278.9,
288.6,
282.7,
288.6,
289.8,
288.8,
291.1,
287.7,
285,
285.8,
287.5,
297.5,
280.1,
277.4,
282.5,
274.8,
267.1,
264,
247.5,
221.1,
224.5,
263.3,
269.7,
266.9,
274.7,
277.2
] # Координата y



plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$v$, мм/с') # Подпись абсцисс
plt.ylabel('$I$, с$^{-1}$') # Подпись ординат

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(0.25))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot3')