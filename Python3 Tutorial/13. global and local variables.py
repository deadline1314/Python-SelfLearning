
x = 6


def example():
    global x
    print(x)
    x += 5
    print(x)
    return x


y = example()
print(y)
