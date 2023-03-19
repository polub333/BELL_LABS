import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


xs = [
    [4.05, 3.5, 3.05, 2.45, 2],
    [4, 3.5, 2.95, 2.55, 1.95],
    [4, 3.5, 3.05, 2.5, 2],
    [4.4, 4, 3.5, 3, 2.5]
]

ys = [
    [3, 2.38, 1.93, 1.31, 0.89],
    [2.72, 2.23, 1.63, 1.26, 0.7],
    [2.55, 1.95, 1.52, 1.09, 0.73],
    [2.5, 2.19, 1.72, 1.33, 1]
]

ts = [295, 303, 313, 323]

for i in range(4):
    x = xs[i]
    y = ys[i]
    t = ts[i]
    plt.figure(figsize=(10,7))  #Размер изображения
    plt.title(f'График зависимости разности температуры от разности давления для T = {t}K') # Заголовок

    plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

    plt.xlabel('$\Delta P$, атм') # Подпись абсцисс
    plt.ylabel('$\Delta T$, К') # Подпись ординат

    yerr = [0.018*_y for _y in y]  # Погрешность по y
    xerr = [0.05 for _x in x] # Погрешность по x
    plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

    p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
    p_f = np.poly1d(p)
    plt.plot(x, p_f(x))
    print(p_f)


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

    plt.savefig(f'plt_U_{i}')


# ==================================================================

x = [0.00339, 0.0033, 0.003195, 0.003096]
y = [1.028, 0.992, 0.894, 0.802]

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости коэффициента Джоуля-Томсона от обратной темепературы') # Заголовок

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$\frac{1}{T}, K^{-1}$') # Подпись абсцисс
plt.ylabel(r'$\mu_{д-т}$, $\frac{K}{атм}$') # Подпись ординат

yerr = [0.03 for _y in y]  # Погрешность по y
xerr = [0.00006 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.xaxis.set_minor_locator(MultipleLocator(0.000025))
ax.xaxis.set_major_locator(MultipleLocator(0.0001))
ax.yaxis.set_minor_locator(MultipleLocator(0.025))
ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('main_plot')
#plt.show()