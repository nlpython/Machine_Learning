import numpy as np
import matplotlib.pyplot as mp
import xarray as xarray

# xarray: <序列> 水平坐标序列
# yarray: <序列> 垂直坐标序列

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([12, 39, 36, 25, 13, 4])


mp.plot(x, y)
# 显示图表
mp.show()

# 绘制水平线和垂直线
# vertical 绘制垂直线
mp.vlines(25, 5, 45)
# horizotal 绘制水平线
mp.hlines(25, 5, 35, color='green')
mp.hlines([10, 20, 30 ,40], 1, 6)
mp.hlines([10, 20, 30, 40], [10, 20, 30, 40], [20, 30, 40, 50])
mp.show()