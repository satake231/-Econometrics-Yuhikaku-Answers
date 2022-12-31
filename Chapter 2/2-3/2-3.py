import numpy as np
import matplotlib.pyplot as plt

a = np.array([[0, 2, 3, 2, 5, 1, 5, 2, 4, 6],
                  [2, 5, 4, 3, 4, 3, 4, 3, 5, 7]])

x = a[0]
y = a[1]

cov = np.cov(x, y)

corr = np.corrcoef(a)

print("covariance = {}".format(cov[0][1]), "\ncorrelation = {}".format(corr[0][1]))
#%%
# 散布図
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter plot")
#%%
