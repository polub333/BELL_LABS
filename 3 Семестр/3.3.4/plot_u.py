import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.optimize import curve_fit

def func(x, a):
    return a * x

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости $U_\perp$ от $B$') # Заголовок

x = [177.4, 317.2, 521, 659.7, 877.3, 945.4, 1002.1, 1075.5] # Координата x

#x = [0.16, 0.3, 0.5, 0.66, 0.9, 1.05, 1.19, 1.43]
#x = [_x*863.548 for _x in x]

y = [[38, 55, 78, 95, 116, 127, 134, 142],
     [77, 110, 158, 194, 241, 261, 278, 294],
     [106,	150,	212,	260,	327,	352,	371,	394],
     [150,	221,	317,	386,	486,	521,	555,	586],
     [178,	253,	367,	454,	558,	606,	642,	681],
     [209,	294,	416,	514,	639,	694,	735,	777],
     [230,	325,	467,	583,	713,	777,	825,	872],
     [250,	361,	527,	646,	798,	866,	917,	971]] # Координата y

y[0] = [_y - 22 for _y in y[0]]
y[1] = [_y - 41 for _y in y[1]]
y[2] = [_y - 55 for _y in y[2]]
y[3] = [_y - 80 for _y in y[3]]
y[4] = [_y - 93 for _y in y[4]]
y[5] = [_y - 105 for _y in y[5]]
y[6] = [_y - 118 for _y in y[6]]
y[7] = [_y - 131 for _y in y[7]]

lines = [0, 0, 0, 0, 0, 0, 0, 0]
labels = ['0.14 мА', '0.3 мА', '0.4 мА', '0.6 мА',
          '0.7 мА', '0.8 мА', '0.9 мА', '1.0 мА']

for i in range(8):
    #lines[i], = plt.plot(x, y[i], label=i, c='green')

    #p = np.polyfit(x, y[i], deg=1) # Построение кривой по мнк
    #p_f = np.poly1d(p)
    popt, pcov = curve_fit(func, x, y[i])
    plt.plot(x, func(x, popt))
    lines[i], = plt.plot(x, func(x, popt), label=labels[i])
    plt.scatter(x, y[i], s=18, c=lines[i].get_color())  # Экспериментальные точки на графике
    print(popt[0])



plt.xlabel('$B$, мТл') # Подпись абсцисс
plt.ylabel('$U$, мкВ') # Подпись ординат

'''
yerr = [0.018*_y for _y in y]  # Погрешность по y
xerr = [0.05 for _x in x] # Погрешность по x
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')
'''
'''

print(p_f)
'''

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.legend(handles=lines)

ax.yaxis.set_minor_locator(MultipleLocator(25))
ax.yaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.set_minor_locator(MultipleLocator(25))
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot_u')