#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

x_values = list(range(1,20))
y_values = [100*(1.5**x) for x in x_values]

plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)


plt.tick_params(axis= 'both', which= 'major', labelsize=14)

plt.axis([0,20,0,11000])

plt.show()