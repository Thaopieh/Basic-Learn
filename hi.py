import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1,1],[1,2], [2,2],[2,3],[3,5]])
y = np.dot(X, np.array([1,2])) + 3
regr = LinearRegression(
   fit_intercept = True, copy_X = True, n_jobs = 2
).fit(X,y)
regr.predict(np.array([[3,5]]))