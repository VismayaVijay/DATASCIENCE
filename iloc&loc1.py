
#program to plot a bar chart showing the choice of
#favourite movie among the people


import numpy as np
import matplotlib.pyplot as plt
objects = ('comedy', 'action', 'romance', 'drama', 'Scifi')
y_pos = np.arange(len(objects))
Types = (4,5,6,1,4)
plt.bar(y_pos, Types, align='center', color='blue')
plt.xticks(y_pos, objects)
plt.ylabel('People')
plt.title('Favourite Type of Movie')
plt.show()