import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,20))  #Размер изображения
plt.title('График зависимости произведения квадрата периода на координату центра масс \n'
          ' от квадрата расстояния от центра масс стержня до точки подвеса') # Заголовок

l = [170, 250, 370, 490, 590, 880, 1050, ] # Координата x
T = [37, 40, 45, 49, 53, 64, 70] # Координата y


plt.scatter(l, T, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$a^2$, см$^2$') # Подпись абсцисс
plt.ylabel(r'$T^2\cdot x_{цм}$, с$^2 \cdot см$') # Подпись ординат

yerr = [0.002+0.4 for y in T]  # Погрешность по y
xerr = [0.1 for x in l] # Погрешность по x
plt.errorbar(l, T, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(l, T, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(l, p_f(l))
print(p_f)


DP = 20
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(2.5))
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.set_minor_locator(MultipleLocator(50))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.show()