import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.ticker import MultipleLocator
from math import log
from statistics import mean

############################################################################################

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости $U$ от времени $t$') # Заголовок

x_40 = []
y_40 = []

with open('40_torr.csv', 'r') as file:
    plotting = csv.reader(file, delimiter = ',')
    for rows in plotting:
        x_40.append(float(rows[0]))
        y_40.append(float(rows[1]))

lny_40 = [log(y) for y in y_40]


av_x = sum(x_40) / len(x_40)
av_lny = sum(lny_40) / len(lny_40)
av_sq_x = sum(x * x for x in x_40) / len(x_40)
av_sq_lny = sum(y * y for y in lny_40) / len(lny_40)
x_lny = []
for i in range(len(x_40)):
    x_lny.append(float(x_40[i] * lny_40[i]))
av_x_lny = sum(x_lny) / len(x_lny)

print("40_torr")
print(av_x, av_lny, av_sq_x, av_sq_lny, av_x_lny, len(x_lny))

plt.plot(x_40, lny_40, color='g')
plt.xlabel(r'$t$, $с$')
plt.ylabel(r'$\ln U$')
plt.savefig('40_torr.png')


############################################################################################

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости $U$ от времени $t$') # Заголовок

x_60 = []
y_60 = []

with open('60_torr.csv', 'r') as file:
    plotting = csv.reader(file, delimiter = ',')
    for rows in plotting:
        x_60.append(float(rows[0]))
        y_60.append(float(rows[1]))

lny_60 = [log(y) for y in y_60]

av_x = sum(x_60) / len(x_60)
av_lny = sum(lny_60) / len(lny_60)
av_sq_x = sum(x * x for x in x_60) / len(x_60)
av_sq_lny = sum(y * y for y in lny_60) / len(lny_60)
x_lny = []
for i in range(len(x_60)):
    x_lny.append(float(x_60[i] * lny_60[i]))
av_x_lny = sum(x_lny) / len(x_lny)

print("60_torr")
print(av_x, av_lny, av_sq_x, av_sq_lny, av_x_lny, len(x_lny))

plt.plot(x_60, lny_60, color='g')
plt.xlabel(r'$t$, $с$')
plt.ylabel(r'$\ln U$')
plt.savefig('60_torr.png')

############################################################################################

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости $U$ от времени $t$') # Заголовок

x_100 = []
y_100 = []

with open('100_torr.csv', 'r') as file:
    plotting = csv.reader(file, delimiter = ',')
    for rows in plotting:
        x_100.append(float(rows[0]))
        y_100.append(float(rows[1]))

lny_100 = [log(y) for y in y_100]


av_x = sum(x_100) / len(x_100)
av_lny = sum(lny_100) / len(lny_100)
av_sq_x = sum(x * x for x in x_100) / len(x_100)
av_sq_lny = sum(y * y for y in lny_100) / len(lny_100)
x_lny = []
for i in range(len(x_100)):
    x_lny.append(float(x_100[i] * lny_100[i]))
av_x_lny = sum(x_lny) / len(x_lny)

print("100_torr")
print(av_x, av_lny, av_sq_x, av_sq_lny, av_x_lny, len(x_lny))

plt.plot(x_100, lny_100, color='g')
plt.xlabel(r'$t$, $с$')
plt.ylabel(r'$\ln U$')
plt.savefig('100_torr.png')

############################################################################################

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости $U$ от времени $t$') # Заголовок

x_150 = []
y_150 = []
with open('150_torr.csv', 'r') as file:
    plotting = csv.reader(file, delimiter = ',')
    for rows in plotting:
        x_150.append(float(rows[0]))
        y_150.append(float(rows[1]))

lny_150 = [log(y) for y in y_150]


av_x = sum(x_150) / len(x_150)
av_lny = sum(lny_150) / len(lny_150)
av_sq_x = sum(x * x for x in x_150) / len(x_150)
av_sq_lny = sum(y * y for y in lny_150) / len(lny_150)
x_lny = []
for i in range(len(x_150)):
    x_lny.append(float(x_150[i] * lny_150[i]))
av_x_lny = sum(x_lny) / len(x_lny)

print("150_torr")
print(av_x, av_lny, av_sq_x, av_sq_lny, av_x_lny, len(x_lny))

plt.plot(x_150, lny_150, color='g')
plt.xlabel(r'$t$, $с$')
plt.ylabel(r'$\ln U$')
plt.savefig('150_torr.png')

############################################################################################

plt.figure(figsize=(10,7))  #Размер изображения
plt.title('График зависимости $U$ от времени $t$') # Заголовок

x_250 = []
y_250 = []

with open('250_torr.csv', 'r') as file:
    plotting = csv.reader(file, delimiter = ',')
    for rows in plotting:
        x_250.append(float(rows[0]))
        y_250.append(float(rows[1]))

lny_250 = [log(y) for y in y_250]


av_x = sum(x_250) / len(x_250)
av_lny = sum(lny_250) / len(lny_250)
av_sq_x = sum(x * x for x in x_250) / len(x_250)
av_sq_lny = sum(y * y for y in lny_250) / len(lny_250)
x_lny = []
for i in range(len(x_250)):
    x_lny.append(float(x_250[i] * lny_250[i]))
av_x_lny = sum(x_lny) / len(x_lny)

print("250_torr")
print(av_x, av_lny, av_sq_x, av_sq_lny, av_x_lny, len(x_lny))

plt.plot(x_250, lny_250, color='g')
plt.xlabel(r'$t$, $с$')
plt.ylabel(r'$\ln U$')
plt.savefig('250_torr.png')
