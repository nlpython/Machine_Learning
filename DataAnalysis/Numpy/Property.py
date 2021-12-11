import numpy as np

a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.shape)    # 行列数
print(a.dtype)    # 元素类型
print(a.ndim)     # 维度, len(shape)
print(a.size)     # 元素数量
print(a.itemsize) # 元素字节数
print(a.nbytes)   # 总字节数 = size x itemsize
print(a.real)     # 复数数组的实部数组
print(a.imag)     # 复数数组的虚部数组
print(a.T)        # 数组的转置
print(a.flat)     # 扁平迭代器
print([x for x in a.flat])
for x in a.flat:
    print(x)

b = np.array([1, 2, 3])
print(b.size)