import quandl
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# ignore necessary warning caused by scipy
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_Change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)
forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
# print(df.head())
print(forecast_out)

x = np.array(df.drop(['label'], 1))
y = np.array(df['label'])
x = preprocessing.scale(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# n_jobs  -> make training process executing in parallel
# -1 means executing as much as possible
clf = LinearRegression(n_jobs=10)

# clf = svm.SVR()

# clf = svm.SVR(kernel='poly')

clf.fit(x_train, y_train)
clf.score(x_test, y_test)
accuracy = clf.score(x_test, y_test)

print(accuracy)
