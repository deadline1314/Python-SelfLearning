import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

# np array and python array are different
# np.loadtxt can load both txt and csv

# x, y = np.loadtxt('exampleTxt.txt', unpack=True, delimiter=',')
x, y = np.loadtxt('exampleCSV.csv', unpack=True, delimiter=',')

plt.plot(x, y)

plt.title('Epic Chart')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()
