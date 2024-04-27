import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def foo(v):
    a = v
    for i in range(len(a)):
        deg = a[i] // 3600
        a[i] -= deg*3600
        min = a[i] // 60
        a[i] -= min*60
        print(deg, min, a[i])

deg_1 = [193, 195, 197, 197, 197]
min_1 = [41, 21, 0, 52, 56]
sec_1 = [38, 19, 58, 48, 21]

deg_2 = [168, 166, 165, 164, 164]
min_2 = [25, 47, 10, 14, 13]
sec_2 = [8, 31, 50, 44, 59]

for i in range(len(sec_1)):
    sec_1[i] += deg_1[i]*3600 + min_1[i]*60

for i in range(len(sec_2)):
    sec_2[i] += deg_2[i]*3600 + min_2[i]*60


center = 181*3600 + 39

phi_1 = [x-center for x in sec_1]
phi_2 = [center - x for x in sec_2]

phi_1_deg = [x / 3600 for x in phi_1]
phi_2_deg = [x / 3600 for x in phi_2]

phi_deg_avg = [0, 0, 0, 0, 0]
for i in range(len(phi_1_deg)):
    phi_deg_avg[i] = (phi_1_deg[i] + phi_2_deg[i]) / 2

x = [404.7, 435.8, 546.1, 577, 579.1]
y = [np.sin(np.deg2rad(x)) for x in phi_deg_avg]
y_1 = [np.sin(np.deg2rad(x)) for x in phi_1_deg]
y_2 = [np.sin(np.deg2rad(x)) for x in phi_2_deg]

plt.scatter(x, y_1, s=18, c='green')  # Экспериментальные точки на графике
plt.scatter(x, y_2, s=18, c='red')  # Экспериментальные точки на графике


plt.xlabel('$\lambda$, нм') # Подпись абсцисс
plt.ylabel('$\sin \phi$') # Подпись ординат

#yerr = [0.018*_y for _y in y]  # Погрешность по y
#xerr = [0.05 for _x in x] # Погрешность по x
#plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
p_f = np.poly1d(p)
plt.plot(x, p_f(x))
print(p_f)

d = 1 / p_f.coef[0] / 1000
print("d: ", d, " мкм")

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(0.005))
ax.yaxis.set_major_locator(MultipleLocator(0.01))
ax.xaxis.set_minor_locator(MultipleLocator(10))
ax.xaxis.set_major_locator(MultipleLocator(50))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('sin_plot')


print("phi_1:")
foo(phi_1)
print("phi_2")
foo(phi_2)

