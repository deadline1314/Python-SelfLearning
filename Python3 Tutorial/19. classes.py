
class Calculator:
    def __add__(self, y):
        added = self + y
        print(added)

    def __sub__(self, y):
        sub = self - y
        print(sub)

    def __mul__(self, y):
        mult = self * y
        print(mult)

    def __truediv__(self, y):
        div = self / y
        print(div)


Calculator.__mul__(3, 5)
