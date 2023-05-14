import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости давления от времени при ухудшении вакуума') # Заголовок

# ==================================================
# first process

x = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 87] # Координата x
y = [6.9, 12, 20, 28, 36, 43, 50, 57, 65, 72, 77] # Координата y

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$t$, c') # Подпись абсцисс
plt.ylabel(r'P, $10^{-5}$ Торр') # Подпись ординат

yerr = [1 for _y in y]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line1, = plt.plot(x, p_f(x), c="green", label="first process")
print(p_f)

# ==================================================

x = [0, 9, 18, 27, 36, 45, 54, 63, 72, 79] # Координата x
y = [7.5, 16, 25, 33, 41, 49, 57, 64, 72, 78] # Координата y

plt.scatter(x, y, s=18, c='red')  # Экспериментальные точки на графике

yerr = [1 for _y in y]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line2, = plt.plot(x, p_f(x), c="red", label="second process")
print(p_f)

# ==================================================

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.legend(handles=[line1, line2])

ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig("uhudshenie.png")