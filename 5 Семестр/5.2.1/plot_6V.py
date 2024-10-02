import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
#plt.title('График зависимости тока коллектора от напряжения на аноде при задерживающем напряжении $U=6$ B') # Заголовок

x = [4.81,
8.25,
11.39,
14.95,
18.2,
20.1,
21.15,
23.33,
23.53,
23.84,
26.18,
27.22,
28.35,
30.7,
32.13,
35.1,
36.6,
38.62,
39.9,
41.2,
43.4,
46.5
] # Координата x
y = [0.0387,
0.092,
0.1412,
0.1907,
0.228,
0.239,
0.236,
0.208,
0.175,
0.1432,
0.1382,
0.1596,
0.184,
0.2261,
0.252,
0.303,
0.3141,
0.319,
0.3105,
0.3008,
0.2854,
0.2778
] # Координата y


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$U$, В') # Подпись абсцисс
plt.ylabel('$I$, А') # Подпись ординат

yerr = [0.002 for _y in y]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

#p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
#p_f = np.poly1d(p)
#plt.plot(x, p_f(x))
#print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.01))
ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot_6V')