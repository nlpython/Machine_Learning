import numpy as np

# 数组的裁剪
# 将调用数组中小于和大于下限和上限的元素替换为下限和上限
a = np.arange(1, 10)
b = np.clip(a, 3, 8)
b = a.clip(min=3, max=7)
print(b)

# 数组的压缩 (只保留表达式为True)的元素
b = a.compress(a > 5)  # 等价于b = a[a > 5]
print(b)

# 掩码数组
a = np.arange(1, 10)
mask = np.all([a > 3, a < 7], axis=0)  # axis=0表示在垂直方向上
# 等价于 mask = (a > 3) & (a < 7)
print(a[mask])
print(a[(a > 3) & (a < 7)])



