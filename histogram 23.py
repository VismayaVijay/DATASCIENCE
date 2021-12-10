

#To plot a histogram with different formatting and suitable tile and labels

import numpy as np
import matplotlib.pyplot as plt

data_students=[5,15,25,35,15,55]
plt.hist(data_students,bins=[0,10,20,30,40,50,60],weights=[20,10,45,33,6,8],
         facecolor='y',
         edgecolor="red")

plt.title("Histogram for Students data")
plt.xlabel ('Value')
plt.ylabel('Frequency')
plt.savefig("student.png")

plt.show()
