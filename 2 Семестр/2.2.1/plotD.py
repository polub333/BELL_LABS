import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости коэффициента взаимной диффузии от давления') # Заголовок

x = [0.02589, 0.01812, 0.0108, 0.00725, 0.00435] # Координата x
y = [9.94, 6.91, 4.16, 2.94, 1.70] # Координата y


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$\frac{1}{P}$, $Торр^{-1}$') # Подпись абсцисс
plt.ylabel(r'D, $\frac{см^2}{с}$') # Подпись ординат

yerr = [0.938, 0.652, 0.392, 0.277, 0.161]  # Погрешность по y
xerr = [0.001233, 0.000604, 0.000218, 0.000097, 0.000035] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.xaxis.set_minor_locator(MultipleLocator(0.001))
ax.xaxis.set_major_locator(MultipleLocator(0.005))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('D.png')