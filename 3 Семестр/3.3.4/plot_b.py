import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.optimize import curve_fit

def func(x, a):
    return a * x

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости $B$ от $I_м$') # Заголовок

x = [0, 0.16, 0.3, 0.5, 0.66, 0.9, 1.05, 1.19, 1.43] # Координата x
y = [0, 177.4, 317.2, 521, 659.7, 877.3, 945.4, 1002.1, 1075.5] # Координата y


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.ylabel('$B$, мТл') # Подпись абсцисс
plt.xlabel('$I_м$, А') # Подпись ординат

'''
yerr = [0.018*_y for _y in y]  # Погрешность по y
xerr = [0.05 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')
'''

popt, pcov = curve_fit(func, x, y)
plt.plot(x, func(x, popt))
print(popt)
'''
p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)
'''

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot_b')