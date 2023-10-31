import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'Зависимость $2 U$ от $N$') # Заголовок

x = [
    1, 2, 3, 4
    ] # Координата x



y_1 = [
    12.8, 18.3, 22.7, 17.2
    ] # Координата y

y_2 = [9.4, 10.4, 10, 12.2]

plt.scatter(x, y_1, s=18, c='green')  # Экспериментальные точки на графике
plt.scatter(x, y_2, s=18, c='red')  # Экспериментальные точки на графике

plt.ylabel(r'$2 U$, В') # Подпись абсцисс
plt.xlabel(r'$N$') # Подпись ординат

p1 = np.polyfit(x, y_1, deg=1) # Построение кривой по мнк
p_f1 = np.poly1d(p1)

p2 = np.polyfit(x, y_2, deg=1) # Построение кривой по мнк
p_f2 = np.poly1d(p2)

line1, = plt.plot(x, p_f1(x), label='13.0 кГц', c="green")
line2, = plt.plot(x, p_f2(x), label='25,2 кГц', c="red")


DP = 2
ax = plt.gca()

ax.legend(handles=[line1, line2])

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('model_2')