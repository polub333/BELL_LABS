import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.figure(figsize=(10,7))  #Размер изображения

x = [
    0,
-4.5,
-4.19,
-3.84,
-3.5,
-3.12,
-2.79,
-2.4,
-2,
-1.5,
-1.52,
-1.37,
-1.08,
-0.77,
-0.4,
0,
4.53,
4.19,
3.87,
3.51,
3.15,
2.82,
2.43,
2.02,
1.55,
1.54,
1.38,
1.09,
0.78,
0.4
] # Координата x
y = [
   807.2,
1178.2,
1172.2,
1182.7,
1177.4,
1168.4,
1170,
1150.3,
1121.9,
1086.7,
1085.4,
1050.4,
992.7,
909,
823.9,
807.2,
1187.1,
1177.6,
1172.4,
1170.8,
1174.8,
1165.9,
1160.8,
1129.6,
1071.4,
1078.4,
1058.2,
1001.4,
928.7,
840.8
] # Координата y

plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

plt.xlabel('$v$, мм/с') # Подпись абсцисс
plt.ylabel('$I$, с$^{-1}$') # Подпись ординат

DP = 2
ax = plt.gca()

## Характеристики сетки

ax.yaxis.set_minor_locator(MultipleLocator(10))
ax.yaxis.set_major_locator(MultipleLocator(50))
ax.xaxis.set_minor_locator(MultipleLocator(0.25))
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

plt.savefig('plot4')