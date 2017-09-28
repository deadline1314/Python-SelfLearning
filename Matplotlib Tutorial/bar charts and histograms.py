import matplotlib.pyplot as plt

# x = [2, 4, 6, 8, 10]
# y = [6, 7, 8, 2, 4]
#
# x2 = [1, 3, 5, 7, 9]
# y2 = [7, 8, 2, 4, 2]
#
# plt.bar(x, y, label='Bars1', color='r')
# plt.bar(x2, y2, label='Bars2', color='c')

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 42, 48, 95]
# ids = [x for x in range(len(population_ages))]
# plt.bar(ids, population_ages)

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')
plt.legend()
plt.show()
