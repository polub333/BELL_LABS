import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math 

plt.figure(figsize=(10,7))  #Размер изображения

x = [0,
10,
20,
30,
40,
50,
60,
70,
80,
90,
100,
110,
120
] # Координата x

y = [951,
956,
869,
774,
690,
638,
550,
488,
435,
397,
360,
337,
317
]

sigma_y = [6,
5,
10,
8,
5,
10,
10,
4,
7,
8,
5,
5,
2
]

for i in range (0, 13):
    sigma_y[i] = sigma_y[i]/(y[i]*y[i])
x = [1-math.cos(_x*math.pi/180) for _x in x]
y = [1/_y for _y in y]

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$1-\cos\theta$') # Подпись абсцисс
plt.ylabel(r'$\frac{1}{N}$') # Подпись ординат

yerr = sigma_y  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.0001))
ax.yaxis.set_major_locator(MultipleLocator(0.0005))
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot')