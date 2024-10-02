import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
#plt.title('График зависимости тока коллектора от напряжения на аноде при задерживающем напряжении $U=8$ B') # Заголовок

x = [9.3,
13.05,
14.5,
16.6,
17.93,
19.8,
21.05,
21.88,
23.19,
24.14,
24.99,
26.6,
28.54,
30.24,
32.36,
34.6,
35.54,
36.62,
38.14,
39.33,
41.33,
43.34,
44.8,
47.08,
48.99,
51.47
] # Координата x
y = [0.0812,
0.1419,
0.1635,
0.1913,
0.2083,
0.225,
0.2287,
0.2271,
0.2137,
0.12,
0.088,
0.0848,
0.1086,
0.1481,
0.191,
0.234,
0.2478,
0.257,
0.263,
0.2625,
0.249,
0.2356,
0.225,
0.2127,
0.2099,
0.2184
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

plt.savefig('plot_8V')