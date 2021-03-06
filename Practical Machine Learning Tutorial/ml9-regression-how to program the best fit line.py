# m = (avg(x) * avg(y) - avg(x*y)) / (avg(x)^2 - avg(x^2))
# b = avg(y) - m * avg(x)

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


def best_fit_slope_and_intercept(x, y):
    m = ((mean(x) * mean(y)) - mean(x * y)) / (mean(x) ** 2 - mean(x ** 2))
    b = mean(y) - m * mean(x)
    return m, b


m, b = best_fit_slope_and_intercept(xs, ys)
print(m, b)

regression_line = [(m * x) + b for x in xs]

predict_x = 8
predict_y = (m * predict_x) + b

plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color='r')
plt.plot(xs, regression_line)
plt.show()
