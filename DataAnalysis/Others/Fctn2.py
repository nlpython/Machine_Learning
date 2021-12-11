import numpy as np

# 加法乘法通用函数
# add(a, a)         # 两数组相加
# add.reduce(a)     # 求数组的累加和
# add.accumulate(a) # 累加和过程
# add.outer([10, 20, 30], a) # 外加
# 返回调用数组中所有元素的乘积--累乘
# ndarray.prod()
# 返回调用数组中所有元素执行累乘的过程数组
# ndarray.cumprod()
# np.outer([10, 20, 30], a)  # 外积

a = np.arange(1, 10)
print(a, '->a')
print(np.add(a, a), '->add')
print(np.add.reduce(a), '->add.reduce')
print(np.add.accumulate(a), '->add.accumulate')
print(a.prod(), '->prod')
print(a.cumprod(), '->cumprod')
print(np.add.outer([10, 20, 30], a), '->add.outer')
print(np.outer([10, 20, 30], a), '->np.outer')


