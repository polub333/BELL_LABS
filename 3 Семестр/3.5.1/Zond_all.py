import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости тока от напряжения на зонде') # Заголовок

x = [25,	22,	19,	16,	13,	10,	8,	6,	4,	2,	0.7,	-0.7,	-2,	-4,	-6,	-8,	-10,	-13,	-16,	-19,	-22,	-25] # Координата x

y1 = [39.5,	38.7,	37.8,	36.8,	35.7,	33.5,	30.9,	26.3,	19.8,	11.5,	5.2,	-3.4,	-9,	-15.9,	-20.6,	-23.5,	-25,	-26.2,	-27.1,	-27.7,	-28.4,	-29.1] # Координата y
y2 = [28.9,	28.3,	27.5,	26.8,	25.9,	24.3,	22.5,	19.2,	14.5,	8.2,	3.6,	-2.3,	-6.5,	-11.4,	-14.9,	-16.9,	-18,	-19,	-19.6,	-20.2,	-20.7,	-21.2]
y3 = [16.8,	16.2,	15.61,	14.95,	14.16,	13.12,	12.06,	10.48,	8.14,	5.23,	3.19,	-1.96,	-3.98,	-6.33,	-8.03,	-9.08,	-9.74,	-10.53,	-11.15,	-11.62,	-12.05,	-12.41]


y1 = [_y - 5.2 for _y in y1]
y2 = [_y - 3.85 for _y in y2]
y3 = [_y - 2.195 for _y in y3]

plt.scatter(x, y1, s=18, c='green')
plt.scatter(x, y2, s=18, c='red')
plt.scatter(x, y3, s=18, c='blue')

plt.xlabel('$U_з$, В', loc='right') # Подпись абсцисс
plt.ylabel('$I_з$, мкА', loc='top') # Подпись ординат

line1, = plt.plot(x, y1, label='4 мА', c='green')
line2, = plt.plot(x, y2, label='3 мА', c='red')
line3, = plt.plot(x, y3, label='1.5 мА', c='blue')

DP = 2
ax = plt.gca()

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

lines = [line1, line2, line3]
ax.legend(handles=lines)

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(4))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(4))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('zond_all')