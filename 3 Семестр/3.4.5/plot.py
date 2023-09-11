import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import interp1d

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('Начальная кривая намагничивания феррита') # Заголовок

x = [2.8, 2.3, 1.8, 1.4, 0.5, 1.3/4, 0] # Координата x
y = [2.3, 2.2, 2, 1.8, 1.25, 3/4, 0] # Координата y

x = [_x * 45 / (0.25*0.22) * 0.02 for _x in x]
y = [_y * 0.4 / (400*0.0003) * 0.02 for _y in y]

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$H$, A/м') # Подпись абсцисс
plt.ylabel('$B$, T') # Подпись ординат

plt.plot(x, y)



DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.005))
ax.yaxis.set_major_locator(MultipleLocator(0.025))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('fer_plot')