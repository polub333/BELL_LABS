import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График Ферми') # Заголовок


#y = [sqrt(_y_n_bal)/pow(x_p, 3/2) for _]
y_ferm = [0, 0, 324.97, 250.25, 162.54, 58.09, 142.24, 148.29, 138.84, 113.83, 
105.54, 98.99, 86.40, 63.33, 56.21, 40.36, 37.79, 42.35, 41.66, 49.41, 41.27,
39.78, 28.92, 20.98, 0, 0, 0]
x_ferm = [0, 3.1, 12.2, 27.1, 47.2, 72.1, 101.1, 133.8, 169.5, 207.8, 248.3,
290.8, 334.8, 380.2, 426.8, 474.4, 522.8, 572.2, 596.8, 621.8, 647, 672.2, 
697.6, 723.1, 774.5, 826.2, 841.8]

x=x_ferm
y=y_ferm

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$T$, кэВ') # Подпись абсцисс
plt.ylabel(r'$N^{1/2}/p^{3/2}$, $c^{1/2}(c/$кэВ$)^{3/2}$') # Подпись ординат

yerr = [0 for _y in y]  # Погрешность по y
xerr = [0 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

x_pol = [290.8, 334.8, 380.2, 426.8, 635]
y_pol = [98.99, 86.40, 63.33, 56.21, 0]
x_pol_a = [290.8, 334.8, 380.2, 426.8, 635]

p = np.polyfit(x_pol, y_pol, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x_pol_a, p_f(x_pol))
print(p_f)

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(50))
ax.xaxis.set_minor_locator(MultipleLocator(50))
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('fermi.png')