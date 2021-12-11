import numpy as np
import matplotlib.pyplot as mp

# 线性预测
# Ax=B
# x = np.linalg.lstsq(A, B)[0]

# 线性拟合
x = [1, 2, 3, 4, 5, 6, 7]
y = [0.4, 1.5, 3.5, 6.8, 7.5, 8.0, 10.7]
x = np.array(x, 'float')
y = np.array(y, 'float')

mp.figure('Linear', facecolor='lightgray')
mp.scatter(
    x, y,
    color='red',
    s=15,
    alpha=0.6,
    label='dot'
)

x = np.vstack((x, np.ones(x.size, 'float')))
x = x.T
y = y.T

res = np.linalg.lstsq(x, y, rcond=None)[0]

# 绘制趋势线  Y = k*x + b
Y = res[0] * x + res[1]
mp.plot(x, Y, color='dodgerblue', label='Trand_Line')

mp.tight_layout()
mp.legend()
mp.show()