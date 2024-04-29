import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
#plt.title('График зависимости разности температуры от разности давления для T=295K') # Заголовок

x = [90,85,80,75,70,65,60,55,50,45,40,35,30,25,20,8,-2,-12,-22,-32,-42,-52,-62,-72] # Координата x
y = [0.044684358,0.220307407,0.263366419,0.350838375,0.425128973,0.475990279,
0.550154576,0.614066415,0.698863363,0.730296743,0.749615078,0.812889827,
0.888888889,0.888888889,0.88785052,0.774596669,0.737711114,0.791154805,
0.791154805,0.773955788,0.664078309,0.481971261,0.295950173,0.201246118,] # Координата y

x = [np.cos(np.deg2rad(_x)) for _x in x]

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$\cos \beta$') # Подпись абсцисс
plt.ylabel('$V_3$') # Подпись ординат

#yerr = [0.018*_y for _y in y]  # Погрешность по y
#xerr = [0.05 for _x in x] # Погрешность по x
#plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('pol_plot')