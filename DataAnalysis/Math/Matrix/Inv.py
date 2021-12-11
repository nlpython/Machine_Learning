import numpy as np

e = np.mat('1 2 3; 2 3 4; 7 5 6')
# 矩阵的逆
print(e.I)
print(e * e.I)
print('-----------------')

# 把逆矩阵推广到非方阵, 称为广义逆矩阵
m = e[:2, :]
print(m)
print(m.I)
print(m * m.I)
print('-----------------')

# 解方程
prices = np.mat('3 3.2; 3.5 3.6')
totals = np.mat('118.4; 135.2')
# 方法一: 使用numpy提供的API解方程
# x = np.linalg.lstsq(prices, totals)[0]  # 求拟合
x = np.linalg.solve(prices, totals)       # 解方程
print(x, '->API')
# 方法二: 矩阵求逆
x = prices.I * totals
print(x, '->矩阵求逆')
