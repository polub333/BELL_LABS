import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
#plt.title('График зависимости тока коллектора от напряжения на аноде при задерживающем напряжении $U=4$ B') # Заголовок

x = [-0.118,
0.564,
1.867,
2.618,
3,
3.32,
3.616,
4.119,
4.679,
5.355,
5.865,
6.444,
6.748,
7.197,
7.643,
8.396,
8.85,
9.361,
9.865,
10.711
] # Координата x
y = [-0.09,
-0.09,
-0.04,
20.68,
49.89,
61.1,
68.07,
76.26,
81.37,
83.63,
83.82,
82.3,
80.63,
77.4,
73.9,
68.28,
65.68,
64.01,
63.98,
67.72
] # Координата y


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$U_к$, В') # Подпись абсцисс
plt.ylabel(r'$U_с$, В') # Подпись ординат

yerr = [1 for _y in y]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

#p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
#p_f = np.poly1d(p)
#plt.plot(x, p_f(x))
#print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot_33')