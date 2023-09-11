import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import interp1d

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('Начальная кривая намагничивания кремниевого железа') # Заголовок

x = [4.8, 4.2, 3.8, 3.3, 2.6, 2.2, 3*2/5, 3.1/5, 0] # Координата x
y = [3, 2.8, 2.6, 2.5, 2.1, 1.8, 1.9/2, 1.2/4, 0] # Координата y

x = [_x * 20 / (0.11*0.22) * 0.05 for _x in x]
y = [_y * 0.4 / (200*0.0002) * 0.02 for _y in y]

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$H$, A/м') # Подпись абсцисс
plt.ylabel('$B$, T') # Подпись ординат

plt.plot(x, y)



DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(0.25))
ax.xaxis.set_minor_locator(MultipleLocator(10))
ax.xaxis.set_major_locator(MultipleLocator(50))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('sil_plot')