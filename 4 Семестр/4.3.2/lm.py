import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости расстояния до максимума от его порядка') # Заголовок

x1 = [0, 1, 2, 3, 4, 5] # Координата x
y1 = [0.916,1.016,1.132,1.248,1.392,1.5] # Координата y
tmp = y1[0]
y1 = [y - tmp for y in y1]

x2 = [0, 1, 2] # Координата x
y2 = [0.9, 1.244, 1.564]
tmp = y2[0]
y2 = [y - tmp for y in y2]

x3 = [0, 1, 2, 3] # Координата x
y3 = [0.876, 1.028, 1.192, 1.328]
tmp = y3[0]
y3 = [y - tmp for y in y3]

x4 = [0, 1] # Координата x
y4 = [0.928, 1.52]
tmp = y4[0]
y4 = [y - tmp for y in y4]

plt.scatter(x1, y1, s=18, c='green')
plt.scatter(x2, y2, s=18, c='red')
plt.scatter(x3, y3, s=18, c='magenta')
plt.scatter(x4, y4, s=18, c='blue')


plt.xlabel('$m$') # Подпись абсцисс
plt.ylabel('$\Delta x$, мм') # Подпись ординат

#yerr = [0.018*_y for _y in y]  # Погрешность по y
#xerr = [0.05 for _x in x] # Погрешность по x
#plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x1, y1, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line1, = plt.plot(x1, p_f(x1), label='1.036 МГц', c='green')
print(p_f)

p = np.polyfit(x2, y2, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line2, = plt.plot(x2, p_f(x2), label='2.873 МГц', c='red')
print(p_f)

p = np.polyfit(x3, y3, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line3, = plt.plot(x3, p_f(x3), label='1.270 МГц', c='magenta')
print(p_f)

p = np.polyfit(x4, y4, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line4, = plt.plot(x4, p_f(x4), label='5.218 МГц', c='blue')
print(p_f)


DP = 2
ax = plt.gca()
ax.legend(handles=[line1, line2, line3, line4])

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(0.25))
ax.xaxis.set_minor_locator(MultipleLocator(0.2))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('lm')