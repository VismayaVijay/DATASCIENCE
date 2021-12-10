# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(100000)
y = np.random.randn(100000)
size = 50*np.random.randn(100000)
colors = np.random.rand(100000)
plt.scatter(x, y, s=size, c=colors)
plt.show()