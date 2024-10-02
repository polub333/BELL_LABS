import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
#plt.title('График зависимости тока коллектора от напряжения на аноде при задерживающем напряжении $U=4$ B') # Заголовок

x = [4.82, 8.91, 12.72, 15.03, 16.78, 18.40, 20.67, 21.60, 22.69, 23.65, 25.38, 27.02, 28.87, 30.37, 32.35, 34.29, 35.30, 36.86, 38.70, 40.00, 41.63, 44.85] # Координата x
y = [0.0605,
0.1249,
0.175,
0.203,
0.2212,
0.237,
0.2395,
0.2383,
0.218,
0.1792,
0.2022,
0.2278,
0.2587,
0.2833,
0.3172,
0.346,
0.361,
0.3676,
0.37,
0.3595,
0.3505,
0.3495,
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

plt.savefig('plot_4V')