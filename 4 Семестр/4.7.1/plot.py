import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
plt.title(r'График зависимости коэффициента преломления от $\cos^2 \theta$') # Заголовок

x1 = [0.011221475,0.024989095,0.043447203,0.0655446,0.091787201,0.120657545,0.150883409,0.18108771,0.209944823,0.236308728,0.261083983,0.282070524,0.292827431] # Координата x
y1 = [1.639250234,1.637272496,1.640857156,1.650744276,1.650360961,1.651254668,1.654804728,1.661653681,1.671865675,1.685095963,1.694886095,1.70646293,1.736520593] # Координата y

x2 = [0.013823261,0.030417093,0.052583638,0.079772584,0.110361103,0.143731817,0.177480843,0.213143145,0.246853945,0.273125383,0.301154604,0.324607353,0.340633494]
y2 = [1.47694721,1.484011885,1.491510683,1.496309487,1.505088332,1.512916098,1.52577943,1.531613965,1.541820907,1.567413156,1.578104937,1.59073023,1.610060301]

plt.scatter(x1, y1, s=18, c='green')  # Экспериментальные точки на графике
plt.scatter(x2, y2, s=18, c='red')

plt.xlabel(r'$\cos^2 \theta$') # Подпись абсцисс
plt.ylabel(r'$n$') # Подпись ординат

#yerr = [0.018*_y for _y in y]  # Погрешность по y
#xerr = [0.05 for _x in x] # Погрешность по x
#plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

x0 = [0.01, 0.02, 0.03, 0.32]
y0 = [1.667, 1.667, 1.667, 1.667]

p = np.polyfit(x0, y0, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line1, = plt.plot(x0, p_f(x0), label='ordinary', c='green')
print(p_f)

p = np.polyfit(x2, y2, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
line2, = plt.plot(x2, p_f(x2), label='extraordinary', c='red')
print(p_f)


DP = 2
ax = plt.gca()
ax.legend(handles=[line1, line2])

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.01))
ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.xaxis.set_minor_locator(MultipleLocator(0.01))
ax.xaxis.set_major_locator(MultipleLocator(0.05))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot')