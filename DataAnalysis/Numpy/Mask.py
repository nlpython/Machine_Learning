import numpy as np

a = np.arange(1, 10)
# 基于bool数组的掩码
mask = [True, False, True, False, True, False, True, False, True]  # 掩码
print(a[mask])   # 形成掩码位置都为True的数组

b = np.arange(1, 100)
print(b[b % 3 == 0])   # b % 3 == 0 就是一个掩码
mask = b % 3 == 0;
print(mask)
mask = (b % 3 == 0) & (b % 7 == 0)     # 只能用 & 不能用 and
print(b[mask])

# 基于索引的掩码
names = np.array(['Apple', 'Huawei', 'MI', 'Oppo', 'Vivo'])
rank = [1, 0, 3, 4, 2]   # 重新排名
print(names[rank])

a = np.arange(1, 10)
mask = np.all([a > 3, a < 7], axis=0)  # axis=0表示在垂直方向上
mask = (a > 3) & (a < 7)
print(a[mask])


