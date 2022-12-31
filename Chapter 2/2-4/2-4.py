import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 5, 6, 7])
P = np.array([1/5, 1/4, 3/10, 1/4])

Ex = sum(x * P)
var = sum((x - Ex) ** 2 * P)

print("Expectation = {}\nVariance = {}".format(Ex, var))
#%%
# 分布関数
plt.bar(x=x, height=P)
plt.xlabel("Values")
plt.ylabel("Possibility")
plt.title("Distribution function")
#%%
