#To plot a simple histogram of random values with bins as 25


import matplotlib.pyplot as plt
import numpy as np
y = np.random.randn(1000)
plt.hist(y,25,edgecolor="red")#(bins=25 and edges color as red)
plt.show()