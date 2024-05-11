import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
#plt.title('График зависимости разности температуры от разности давления для T=295K') # Заголовок

x = [1, 2, 3, 4, 5, 7] # Координата x
y = [37.24513391,41.64132563,43.67379077,43.00697618,41.64132563,42.66966135] # Координата y

y = [_y/100 for _y in y]

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$n$') # Подпись абсцисс
plt.ylabel(r'$\xi_n$, мм') # Подпись ординат

#yerr = [0.018*_y for _y in y]  # Погрешность по y
#xerr = [0.05 for _x in x] # Погрешность по x
#plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line1, = plt.plot(x, p_f(x), label='experimental')
print(p_f)

x1, y1 = [1, 7], [0.34, 0.34]
line2, = plt.plot(x1, y1, label='actual')

plt.axis([0.5, 7.5, 0, 0.5])


DP = 2
ax = plt.gca()
ax.legend(handles=[line1, line2])
## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('1')