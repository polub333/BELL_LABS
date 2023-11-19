import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости тока от напряжения на зонде ($I = 1.5$ мА)') # Заголовок

x = [25,	22,	19,	16,	13,	10,	8,	6,	4,	2,	0.7,	-0.7,	-2,	-4,	-6,	-8,	-10,	-13,	-16,	-19,	-22,	-25] # Координата x
y = [16.8,	16.2,	15.61,	14.95,	14.16,	13.12,	12.06,	10.48,	8.14,	5.23,	3.19,	-1.96,	-3.98,	-6.33,	-8.03,	-9.08,	-9.74,	-10.53,	-11.15,	-11.62,	-12.05,	-12.41]

y = [_y - 2.195 for _y in y]

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

plt.savefig('zond_3')