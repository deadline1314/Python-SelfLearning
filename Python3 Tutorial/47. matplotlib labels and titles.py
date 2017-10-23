import matplotlib.pyplot as plt

x = [5, 7, 3, 5]
y = [4, 8, 4, 2]

print(len(x))
print(len(y))

plt.plot(x, y)
plt.title('Epic Chart')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()
