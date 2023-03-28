import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from math import exp

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости давления насыщенного пара от температуры') # Заголовок

x_n_lin = [0.003411, 0.003377, 0.003356, 0.003333, 0.00331, 0.003289,
     0.003268, 0.003252, 0.003236, 0.003221, 0.003205, 0.00319]
y_n_lin = [7.64, 7.70, 7.87, 8.00, 8.14, 8.26, 8.40, 8.51,
           8.58, 8.68, 8.76, 8.85] # Нагрев Линия

x_o_lin = [0.003205, 0.003221, 0.003236, 0.003252, 0.003268, 0.003284, 0.0033,
           0.003317, 0.003333, 0.00335, 0.003367, 0.003384, 0.003401]
y_o_lin = [8.81, 8.71, 8.62, 8.55, 8.47, 8.38, 8.3, 8.20,
           8.1, 7.99, 7.88, 7.74, 7.66] # Охлаждение Линия


plt.scatter(x_n_lin, y_n_lin, s=18, c='green')  # Экспериментальные точки на графике
plt.scatter(x_o_lin, y_o_lin, s=18, c='red')  # Экспериментальные точки на графике

plt.ylabel(r'$\ln P$') # Подпись абсцисс
plt.xlabel(r'$\frac{1}{T}$, $К^{-1}$') # Подпись ординат

yerr = [0.004 for x in x_n_lin]  # Погрешность по y
xerr = [1.1*(10**(-6)) for y in y_n_lin] # Погрешность по x
plt.errorbar(x_n_lin, y_n_lin, xerr=xerr, yerr=yerr, fmt=" ", color='k')

yerr = [0.004 for x in x_o_lin]  # Погрешность по y
xerr = [1.1*(10**(-6)) for y in y_o_lin] # Погрешность по x
plt.errorbar(x_o_lin, y_o_lin, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x_n_lin, y_n_lin, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x_n_lin, p_f(x_n_lin))
print(p_f)

p = np.polyfit(x_o_lin, y_o_lin, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x_o_lin, p_f(x_o_lin))
print(p_f)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.00001))
ax.xaxis.set_major_locator(MultipleLocator(0.00005))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('lin_plot')



# ============================================================== #
# ============================================================== #
# ============================================================== #



plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости давления насыщенного пара от температуры') # Заголовок

x_n_exp = [293.2, 296.1, 298, 300, 302.1, 304, 306, 307.5, 309, 310.5, 312, 313.5]
y_n_exp = [2091, 2224, 2624, 2997, 3449, 3902,
           4462, 4968, 5367, 5900, 6433, 6993] # Нагрев Экспонента
y_n_ap = [1.8363*(10**(-5))*exp(0.0630672*x) for x in x_n_exp] # Приближение нагрев

x_o_exp = [312, 310.5, 309, 307.5, 306, 304.5, 303,
           301.5, 300, 298.5, 297, 295.5, 294]
y_o_exp = [6673, 6033, 5527, 5154, 4781, 4355, 4035,
           3636, 3290, 2943, 2650, 2304, 2117] # Охлаждение Экспонента
y_o_ap = [1.88*(10**(-5))*exp(0.06318*x) for x in x_o_exp] # Приближение охлажд



plt.scatter(x_n_exp, y_n_exp, s=18, c='green')  # Экспериментальные точки на графике
plt.scatter(x_o_exp, y_o_exp, s=18, c='red')  # Экспериментальные точки на графике

plt.ylabel(r'$P$, Па') # Подпись абсцисс
plt.xlabel(r'$T$, $К$') # Подпись ординат

yerr = [13.32 for x in x_n_exp]  # Погрешность по y
xerr = [0.1 for y in y_n_exp] # Погрешность по x
plt.errorbar(x_n_exp, y_n_exp, xerr=xerr, yerr=yerr, fmt=" ", color='k')

yerr = [13.32 for x in x_o_exp]  # Погрешность по y
xerr = [0.1 for y in y_o_exp] # Погрешность по x
plt.errorbar(x_o_exp, y_o_exp, xerr=xerr, yerr=yerr, fmt=" ", color='k')

plt.plot(x_n_exp, y_n_ap)

plt.plot(x_o_exp, y_o_ap)


DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(250))
ax.yaxis.set_major_locator(MultipleLocator(1000))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('exp_plot')