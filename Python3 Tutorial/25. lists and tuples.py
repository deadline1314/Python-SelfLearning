# list can be modified, tuple can not

# tuple -> iterate fast
x = 5, 6, 2, 6
y = (5, 6, 2, 6)

# list
z = [5, 6, 2, 6]

print(x[1])  # 6
print(y[2], y[3])  # 2, 6


def example_func():
    return 15, 6


one, two = example_func()


