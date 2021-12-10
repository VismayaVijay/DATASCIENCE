

#To plot a box plot for frequency distribution of marks

import matplotlib.pyplot as plt
value1 = [43,76,34,63,56,82,87,55,64,87]
value2 = [34,45,34,23,43,76,26,18,24,74]
value3 = [23,89,12,78,72,89,25,69,68,86]
value4 = [99,73,70,16,81,61,88,98,10,87]
box_plot_data=[value1,value2,value3,value4]
box=plt.boxplot(box_plot_data,vert=1,patch_artist=True,labels=['course1','course2','course3','course4'],)
colors = ['cyan','purple','darkblue','darkgreen']
for patch, color in zip(box['boxes'],colors ):
    patch.set_facecolor(color)


plt.show()