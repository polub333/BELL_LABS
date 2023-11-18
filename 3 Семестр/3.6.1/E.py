import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости амплитудного коэффициента фильтрации от частоты') # Заголовок

x = [1,	2,	3,	4,	5,	6,	7,	8] # Координата x
y = [17.4,	246.3,	20.7,	267.8,	30.22,	245.5,	34,	252] # Координата y
y1 = [0,	80.3,	0,	45.12,	0,	25.66,	0,	21.11]

for i in range(0, 8):
    y[i] = y1[i] / y[i]

x = [_x*0.333 for _x in x]


plt.xlabel(r'$\frac{1}{\nu}$, МГц$^{-1}$') # Подпись абсцисс
plt.ylabel(r'$\frac{a_{ф}}{a_{0}}$') # Подпись ординат


xx = [0, 0, 0, 0]
yy = [0, 0, 0, 0]

for i in range(0, 4):
    xx[i] = x[2*i+1]
    yy[i] = y[2*i+1]


xx = [1/_xx for _xx in xx]

plt.scatter(xx, yy, s=18, c='green')  # Экспериментальные точки на графике

p = np.polyfit(xx, yy, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(xx, p_f(xx))
print(p_f)

#plt.plot(xx, yy)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.025))
ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('E')
