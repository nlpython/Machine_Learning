import numpy as np

# 矩阵是numpy.matrix类类型的对象, 该类继承自numpy.ndarray,
# 任何针对多维数组的操作, 对矩阵同样有效, 但是作为子类矩阵又
# 结合其自身特点, 做了必要的扩充, 比如: 乘法计算, 求逆等

# 矩阵的创建

# 如果copy的值为True(缺省), 所得到的矩阵对象与参数中的源容器拥有独立的数据拷贝(数据不共享)
# numpy.matrix(
#     ary,            # 任何可被解释为矩阵的二维容器
#     copy=True       # 是否复制数据(缺省值为True, 即复制新数据)
# )

# 等价于: numpy.matrix(...., copy=False)
# 由该函数创建的矩阵对象一个共享数据, 无法拥有各自独立的数据
# numpy.mat(任何可被解释为矩阵的二维容器)

# 该函数可以接受字符串形式的矩阵描述:
# 数据项通过空格或逗号分隔, 数据行通过分号分隔. 例如: '1, 2, 3; 4, 5, 6'
# numpy.mat('.....')

ary = np.arange(1, 10).reshape(3, 3)
m1 = np.matrix(ary, copy=False)
print(m1)
print('-------------------------')

m2 = np.mat(ary)
print(m2)
m2[1, 1] = 123
print(ary)
print('-------------------------')

m3 = np.mat('1 2 3; 4 5 6')
print(m3)