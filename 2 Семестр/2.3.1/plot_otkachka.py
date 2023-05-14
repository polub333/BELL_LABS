import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости давления от времени при откачке системы') # Заголовок

# ============================================
# first process, befor izlom

x = [0, 4, 8, 12, 16, 20] # Координата x
y = [4.34, 4.04, 3.21, 2.63, 2.30, 2.14] # Координата y

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$t$, c') # Подпись абсцисс
plt.ylabel(r'$\ln P$') # Подпись ординат

yerr = [0.01, 0.01, 0.04, 0.07, 0.1, 0.1]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line1, = plt.plot(x, p_f(x), label="first process", c="green")
print(p_f)

# ============================================
# first process, after izlom

x = [24, 28, 32, 36]
y = [2.067, 2.041, 2.028, 2.015]

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

yerr = [0.13 for _y in y]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x), c="green")
print(p_f)

# ============================================
# second process, befor izlom

x = [0, 4, 8, 12, 16, 20, 24]
y = [4.35, 4.04, 3.21, 2.63, 2.3, 2.14, 2.08]

plt.scatter(x, y, s=5, c='red')  # Экспериментальные точки на графике

yerr = [0.01, 0.01, 0.04, 0.07, 0.1, 0.1, 0.1]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line2, = plt.plot(x, p_f(x), c="red", label="second process")
print(p_f)

# ============================================
# second process, after izlom

x = [28, 32, 36, 40, 45]
y = [2.041, 2.028, 2.028, 2.015, 2]

plt.scatter(x, y, s=5, c='red')  # Экспериментальные точки на графике

yerr = [0.13 for _y in y]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line2, = plt.plot(x, p_f(x), c="red", label="second process")
print(p_f)

# ===========================================

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.legend(handles=[line1, line2])

ax.xaxis.set_minor_locator(MultipleLocator(2.5))
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig("otkachka.png")