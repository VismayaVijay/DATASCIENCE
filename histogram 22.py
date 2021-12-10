

#To plot a histogram for number of students with no value for range 40-50

import matplotlib.pyplot as plt

data_students=[5,15,25,35,15,55]
plt.hist(data_students,bins=[0,10,20,30,40,50,60],weights=[20,10,45,33,6,8],
         edgecolor="red")

plt.show()