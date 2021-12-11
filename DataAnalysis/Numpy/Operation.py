import numpy as np
import matplotlib.pyplot as mp

# 逻辑运算
stocks = np.random.normal(0, 1, (8, 10))
# print(stocks)
# 返回数组值大于0.5的布尔表
print(stocks[stocks > 0.5])
# 统一赋值为0.1
stocks[stocks > 0.5] = 0.1
print(stocks)

print('-' * 45)

# np.all() 只有当全部为True才返回True, 否则返回False
print(np.all(stocks > -10))
# np.any() 只有当全部为False才返回False, 否则返回True
print(np.any(stocks > 2))
# np.where()
# 判断前四只股票的前四天数据, 大于0的置为1, 否则为0
stocks = np.where(stocks[:4, :4] > 0, 1, 0)
print(stocks)
print((stocks < 5) & (stocks > 0))

print('-' * 45)

# 统计方法      max, min, mean, var, std, median
stocks = np.random.normal(0, 1, (8, 10))
print('前四天每只股票的最大值:', stocks[:, :4].max(axis=1)) # axis=1表示按行, 0表示按列
print('最大值所在位置:', stocks[:, :4].argmax(axis=1))

# 读取文件
test = np.genfromtxt('./data.csv', delimiter=',')

