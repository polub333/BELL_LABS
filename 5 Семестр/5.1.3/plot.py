import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
#plt.title('График зависимости тока коллектора от напряжения на аноде при задерживающем напряжении $U=4$ B') # Заголовок

x = [0.602,
2.073,
2.477,
2.624,
2.712,
2.8,
2.899,
3.171,
3.312,
3.614,
3.744,
3.964,
4.143,
4.31,
4.701,
4.804,
5.196,
5.36,
5.559,
5.869,
6.269,
6.503,
7.183,
8.078,
8.762,
9.231,
10.204,
11.646
] # Координата x
y = [-0.1,
-0.07,
1.95,
6.33,
10.7,
17,
25.6,
40.85,
47,
54.18,
56.34,
59.28,
61.2,
62.66,
64.23,
64.73,
64.35,
63.78,
63.12,
64.7,
62,
60.4,
54.1,
45.3,
40.12,
37.65,
35.09,
37.92
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

plt.savefig('plot_28')