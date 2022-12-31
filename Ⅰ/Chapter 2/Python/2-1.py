import numpy as np
from scipy import stats

array = np.array([12, 15, 9, 17, 5, 8, 10, 12, 6, 3, 10, 11, 20, 6, 8, 10, 13, 10, 11, 4])

mean = np.mean(array)

var = np.var(array)

mdn = np.median(array)

count = stats.mode(array, axis=None)
mode = count[0][0]

print(" mean={} \n variance={} \n median={} \n mode={}".format(mean, var, mdn, mode))
#%%
