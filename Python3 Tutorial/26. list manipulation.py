x = [6, 5, 2, 1, 4, 7, 8, 2, 1]

x.append(2)
x.insert(4, 10)
x.remove(2)   # remove the first "2"
x.remove(x[2])  # remove the index 2 element
print(x)
print(x[5:7])   # print index [5, 7)
print(x[-1])   # print the end list element
print(x.index(1))  # find the first index of "1"
print(x.count(2))  # count the number of "2"

x.sort()
print(x)

y = ['Janet', 'Jessy', 'Kelly', 'Alice', 'Joe', 'Bob']
y.sort()
print(y)
