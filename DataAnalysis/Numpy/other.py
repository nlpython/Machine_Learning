import numpy as np
import matplotlib.pyplot as mp

# 生成随机分布
data1 = np.random.uniform(-10, 10, 1000)
mp.hist(data1, 10)
mp.show()

# 生成正态分布
data2 = np.random.normal(0, 1, 10000)
mp.hist(data2, 10)
mp.show()

# 数组去重
data3 = np.array([[1, 2, 3], [3, 4, 1]])
data3 = np.unique(data3)
print(data3)
