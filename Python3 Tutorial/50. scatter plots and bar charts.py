import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5, 7, 3, 2]
y = [4, 8, 4, 2]

x2 = [4, 8, 9, 1]
y2 = [9, 3, 1, 2]

print(len(x))
print(len(y))

# plt.scatter(x, y, color='c', label='line one')
# plt.scatter(x2, y2, color='b', label='line two')
plt.bar(x, y, color='c', label='line one', align='center')
plt.bar(x2, y2, color='b', label='line two', align='center')
plt.title('Epic Chart')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()

plt.show()
