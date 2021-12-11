import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as mp

# 插值 :  将离散数据连续化
# func = si.interp1d(
#     离散水平坐标,
#     离散垂直坐标,
#     kind=插值算法(缺省为线性插值)
#     线性插值    'linear'
#     三次样条插值 'cubic'
# )

# 原始数据
min_x = -50
max_x = 50
dis_x = np.linspace(min_x, max_x, 15)
dis_y = np.sinc(dis_x)
mp.scatter(dis_x, dis_y, s=60, color='dodgerblue', marker='o', label='Samples')
mp.grid(linestyle=':')


# 通过一系列的散点设计出符合一定规律插值器函数
linear = si.interp1d(dis_x, dis_y, kind='linear')
cubic = si.interp1d(dis_x, dis_y, kind='cubic')
x = np.linspace(min_x, max_x, 2000)
lin_y = linear(x)
cub_y = cubic(x)
mp.plot(x, lin_y, color='red', label='linear inter', alpha=0.8)
mp.plot(x, cub_y, color='green', label='cubic inter')
mp.legend()
mp.show()
