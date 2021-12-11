import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(3, 9).reshape(2, 3)
print('a : ', a)
print('b : ', b)

# 水平方向操作
c = np.hstack((a, b))    # 合并
print(c)
d, e = np.hsplit(c, 2)   # 分割
print(d)
print('----------------------')

# 垂直方向操作
c = np.vstack((a, b))
print(c)
d, e = np.vsplit(c, 2)
print('----------------------')

# 深度方向操作
c = np.dstack((a, b))
print(c)
d, c = np.dsplit(c, 2)
print(d)
print(c)

# 通过axis作为关键字参数指定组合的方向, 取值如下:
# 若待组合数组都是二维数组:
#     0: 垂直方向组合
#     1: 水平方向组合
# 若待组合数组都是三维数组
#     0: 垂直方向组合
#     1: 水平方向组合
#     2: 深度方向组合
# np.concatenate((a, b), axis=0)
# np.split(c, 2, axis=1)

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4])

# 填充b数组使其长度与a相同, 头部补0个元素, 尾部补1个元素, 默认补constant_values
b = np.pad(b, pad_width=(0, 1), mode='constant', constant_values=-1)
print(b)
# 垂直方向完成组合操作, 生成新数组
c = np.vstack((a, b))
print(c)
print('------------------')

a = np.arange(1, 9)     # [1 2 3 4 5 6 7 8]
b = np.arange(9, 17)    # [9 10 11 12 13 14 15 16]
# 把两个数组摞在一起成两行
c = np.row_stack((a, b))
print(c)
# 把两个数组竖起来并成两列
d = np.column_stack((a, b))
print(d)
