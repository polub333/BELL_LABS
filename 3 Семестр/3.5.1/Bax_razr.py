import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости тока разряда от напряжения') # Заголовок

x1 = [23.7,	23.2,	21.8,	20.4,	19.5,	18.4,	17,	14.9,	12.5] # Координата x
y1 = [2.01,	2.21,	2.49,	2.74,	2.92,	3.1,	3.31,	3.58,	3.87] # Координата y

x2 = [15.8,	17.4,	18.8,	19.9,	21.5,	23,	23.6]
y2 = [3.49,	3.27,	3.04,	2.84,	2.55,	2.28,	2.11]

x1 = [_x * 10 for _x in x1]
x2 = [_x * 10 for _x in x2]

plt.scatter(x1, y1, s=18, c='green')  # Экспериментальные точки на графике
plt.scatter(x2, y2, s=18, c='red')

plt.xlabel('$U_р$, В') # Подпись абсцисс
plt.ylabel('$I_р$, мА') # Подпись ординат

'''
p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)
'''

line1, = plt.plot(x1, y1, c='green', label="нарастание тока")
line2, = plt.plot(x2, y2, c='red', label="убывание тока")

lines = [line1, line2]

DP = 2
ax = plt.gca()
ax.legend(handles=lines)

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.xaxis.set_minor_locator(MultipleLocator(10))
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('bax_razr')