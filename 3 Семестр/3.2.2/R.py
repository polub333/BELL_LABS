import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'Зависимость активного сопротивления катушки от резонансной частоты') # Заголовок

x = [27.3,	23,	21.06,	19.45,	17.61,	16] # Координата x
y = [6.826960572,	3.923266574,	3.783407794,	4.455445693,	3.570756946,	3.489517203] # Координата y

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике.

plt.xlabel(r'$\nu_{0n}$, кГц') # Подпись абсцисс
plt.ylabel(r'$R_L$, Ом') # Подпись ординат

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)

DP = 2
ax = plt.gca()
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0.6*16)

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('r')