import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'Зависимость $\delta \phi$ от $\nu$') # Заголовок

x = [
    1, 5, 9, 13, 17, 21, 25, 29, 35
    ] # Координата x



y = [
    0.175929189,	1.068141502,	7.244512659,	13.54654752,
    20.13132572,	26.66332517,	32.86105916,	39.15681083,
    45.56565985
    ] # Координата y

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.ylabel(r'$\delta \phi$') # Подпись абсцисс
plt.xlabel(r'$\nu$, кГц') # Подпись ординат

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('model_1')