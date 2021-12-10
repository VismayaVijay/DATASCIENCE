
import numpy as np

import matplotlib.pyplot as plt
objects = {'python','c++','java','perl','scala','lisp'}
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.barh(y_pos, performance, align='center', color='r')
ply.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Programmimng language usage')

plt.show()