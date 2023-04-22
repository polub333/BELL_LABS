import numpy as np
import matplotlib.pyplot as plt
import csv
import math
from matplotlib.ticker import MultipleLocator

names = ["40.csv", "60.csv", "100.csv", "150.csv", "250.csv"]

for name in names:

    plt.figure(figsize=(10,7))  #Размер изображения
    plt.title(f'График зависимости напряжения от времени при давлении P$\\approx${name[:-4]} Торр') # Заголовок

    x = []
    y = []


    with open(name, encoding='utf-8') as file:
        reader_object = csv.reader(file, delimiter=",")
        count = 0
        for row in reader_object:        
            if count < 2:
                count += 1
            else:
                x.append(float(row[0]))
                y.append(math.log(float(row[1])))
            

    x_2 = [_x*_x for _x in x]
    y_2 = [_y*_y for _y in y]
    xy = []
    for i in range(0, len(x)):
        xy.append(x[i]*y[i])

    x_avg = sum(x)/len(x)
    y_avg = sum(y)/len(y)
    x_2_avg = sum(x_2)/len(x)
    y_2_avg = sum(y_2)/len(y)
    xy_avg = sum(xy)/len(xy)

    k = (xy_avg - x_avg*y_avg)/(x_2_avg - x_avg**2)
    sigma_k = math.sqrt((y_2_avg - y_avg**2)/(x_2_avg - x_avg**2) - k**2)/math.sqrt(len(x))
    print(k, sigma_k)

    plt.scatter(x, y, s=18, c='green')  # Экспериментальные точки на графике

    plt.xlabel('$t$, с') # Подпись абсцисс
    plt.ylabel('$\ln U$') # Подпись ординат

    yerr = [0.2/(math.exp(_y)) for _y in y]  # Погрешность по y
    xerr = [0 for _x in x] # Погрешность по x
    plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=" ", color='k')

    p = np.polyfit(x, y, deg=1) # Построение кривой по мнк
    p_f = np.poly1d(p)
    plt.plot(x, p_f(x))
    #print(p_f)

    DP = 2
    ax = plt.gca()

    ## Характеристики сетки

    ax.xaxis.set_minor_locator(MultipleLocator((x[-1] - x[0])/25))
    ax.xaxis.set_major_locator(MultipleLocator((x[-1] - x[0])/5))
    ax.yaxis.set_minor_locator(MultipleLocator((y[0] - y[-1])/25))
    ax.yaxis.set_major_locator(MultipleLocator((y[0] - y[-1])/5))
    ax.yaxis.grid(True,'major',linewidth=2/DP,linestyle='-',color='#d7d7d7')
    ax.xaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
    ax.yaxis.grid(True,'minor',linewidth=1/DP,linestyle='-',color='#d7d7d7')
    ax.xaxis.grid(True,'major',linewidth=1/DP,linestyle='-',color='#d7d7d7',zorder=0)

    plt.savefig(f'{name[:-4]}.png')  