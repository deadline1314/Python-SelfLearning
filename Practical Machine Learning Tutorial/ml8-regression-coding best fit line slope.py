# m = (avg(x) * avg(y) - avg(x*y)) / (avg(x)^2 - avg(x^2))

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


# plt.scatter(xs, ys)
def best_fit_slope(x, y):
    ret = ((mean(x) * mean(y)) - mean(x * y)) / (mean(x) ** 2 - mean(x ** 2))
    return ret


m = best_fit_slope(xs, ys)
print(m)
