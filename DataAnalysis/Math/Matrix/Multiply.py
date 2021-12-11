import numpy as np

# 矩阵乘法
e = np.arange(1, 10).reshape(3, 3)
print(e * e)    # 数组对应位置相乘
me = np.mat(e)
print(me * me)  # 等价于 np.matmul(e, e)