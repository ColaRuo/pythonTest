# -*- coding: utf-8 -*-
"""
exercise 5
"""

import matplotlib.pyplot as plt

x = range(1, 9)
data1 = [1, 4, 9, 16, 25, 36, 49, 64]
data2 = [1, 2, 3, 6, 9, 15, 24, 39]
data3 = [2, 4, 6]

plt.plot(x, data1, "--", color = "b", linewidth = 1, marker = "o", markersize = 3)
plt.plot(x, data2, "--", color = "r", linewidth = 1, marker = "o", markersize = 3)
plt.xlabel("x-Value", size = 16)
plt.ylabel("y-Value", size = 16)
plt.title("Figure", size = 24)

plt.axis([0, 8, 0, 70])

plt.show()