import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения
#plt.title('График зависимости разности температуры от разности давления для T=295K') # Заголовок

x = [1898,
2156,
2200,
2292,
2272,
2300,
2264,
2320,
2342,
2368,
2390,
2395,
2430,
2438,
2466,
2482,
2497,
2126,
2104,
1940,
1518,
854,
304
] # Координата x
y = [5400,
5852,
5944,
6143,
6096,
6164,
6074,
6217,
6266,
6334,
6383,
6402,
6507,
6533,
6599,
6678,
6717,
5791,
5770,
5461,
4916,
4358,
4047
] # Координата y

x.sort()
y.sort()


plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel(r'$\theta^\circ$') # Подпись абсцисс
plt.ylabel(r'$\lambda$, $\AA$') # Подпись ординат


def func(x, p1,p2,p3):
    return p1+(p2/(x-p3))

  

# Here you give the initial parameters for p0 which Python then iterates over
# to find the best fit
popt, pcov = curve_fit(func,x,y,p0=(3800, -1000000, 3000))

print(popt) # This contains your two best fit parameters

# Performing sum of squares
p1 = popt[0]
p2 = popt[1]
p3=popt[2]
residuals = y - func(x,p1,p2,p3)
fres = sum(residuals**2)

print(fres)

xaxis = np.linspace(200, 2550, 1000) # we can plot with xdata, but fit will not look good 
#p1 = 3800.0
#p2=-1000000.0
#p3=3000.0
curve_y = func(xaxis,p1,p2,p3)
print(func(1000, 3800, -1, 3000))
#plt.plot(x,y,'*')
plt.plot(xaxis,curve_y)

#yerr = [0.018*_y for _y in y]  # Погрешность по y
#xerr = [0.05 for _x in x] # Погрешность по x
#plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

#p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
#p_f = np.poly1d(p)
#plt.plot(x, p_f(x))
#print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(50))
ax.yaxis.set_major_locator(MultipleLocator(250))
ax.xaxis.set_minor_locator(MultipleLocator(50))
ax.xaxis.set_major_locator(MultipleLocator(250))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('grad')