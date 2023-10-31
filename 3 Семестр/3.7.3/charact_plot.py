import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'Зависимость $k(\omega)^2-\alpha(\omega)^2$ от $\omega^2$') # Заголовок

x = [
    986.9604401,	1934.442463,	3197.751826,	4776.88853,	7737.76985,	
    11409.26269,	15791.36704,	20884.08291,	26687.4103,	33201.34921,
    40425.89963,	48361.06157,	57006.83502
    ] # Координата x


y = [
    -0.005050709,	0.003686051,	0.02161988,	0.046077775,	0.097115814,
     0.168798514,	0.254543112,	0.36233473,	0.482551556,	0.627954565,
     0.791797308,	0.974058497,	1.135649977
    ] # Координата y


x = [_x/1000 for _x in x]

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.ylabel(r'$k(\omega)^2-\alpha(\omega)^2$, $10^{-4}$ см$^{-2}$') # Подпись абсцисс
plt.xlabel(r'$\omega^2$, $10^3$ МГц$^2$') # Подпись ординат

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('charact_plot')