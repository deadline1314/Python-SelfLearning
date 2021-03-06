import matplotlib.pyplot as plt
from matplotlib import style

# style.use('ggplot')

x = [5, 7, 3, 5]
y = [4, 8, 4, 2]

x2 = [4, 8, 9, 1]
y2 = [9, 3, 1, 2]

print(len(x))
print(len(y))

plt.plot(x, y, 'b', linewidth=5, label='line one')
plt.plot(x2, y2, 'c', linewidth=10, label='line two')
plt.title('Epic Chart')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()

plt.grid(True, color='k')

plt.show()
