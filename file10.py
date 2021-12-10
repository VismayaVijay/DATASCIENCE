# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import matplotlib.pyplot as plt
weight =[83.3,74,64.5,79,90,84.8,84,88,66,77,79,90.5,74.3,90,73]
height =[167,113.7,124.8,165.5,145.4,155,149,180,169.5,156,167.3,145,185,181,168.3]
plt.scatter(weight,height)
plt.xlabel('weight')
plt.ylabel('height')
plt.title("Scatter plot -height vs weight" ,fontsize=20)
plt.show()