import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости тока от напряжения на зонде ($I = 4$ мА)') # Заголовок

x = [25,	22,	19,	16,	13,	10,	8,	6,	4,	2,	0.7,	-0.7,	-2,	-4,	-6,	-8,	-10,	-13,	-16,	-19,	-22,	-25] # Координата x
y = [39.5,	38.7,	37.8,	36.8,	35.7,	33.5,	30.9,	26.3,	19.8,	11.5,	5.2,	-3.4,	-9,	-15.9,	-20.6,	-23.5,	-25,	-26.2,	-27.1,	-27.7,	-28.4,	-29.1] # Координата y

y = [_y - 5.2 for _y in y]

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$U_з$, В', loc='right') # Подпись абсцисс
plt.ylabel('$I_з$, мкА', loc='top') # Подпись ординат

plt.plot(x, y)


DP = 2
ax = plt.gca()

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(4))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(4))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('zond_1')