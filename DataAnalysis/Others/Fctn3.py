import numpy as np

# # 除法通用函数
# np.divide(a, b)         # a 真除 b
# np.floor(a / b)         # 真值向下取整
# np.ceil(a / b)          # 向上取整
# np.trunc(a / b)         # 去掉小数部分
# np.round(a / b)         # 四舍五入

a = np.array([20, 20, -20, -20])
b = np.array([3, -3, 6, -6])
# 真除
c = np.true_divide(a, b)
c = np.divide(a, b)
c = a / b
print('array:', c)
# 对ndarray做floor操作
d = np.floor(a / b)
d = np.floor_divide(a, b)
print('floor_divide:', d)
# 对ndarray做ceil操作
e = np.ceil(a / b)
print('ceil:', e)
# 对ndarray做trunc操作
f = np.trunc(a / b)
print('trunc:', f)
# around
g = np.around(a / b)
print('around:', g)
