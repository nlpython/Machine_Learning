import numpy as np

a = np.arange(1, 9)
a.shape = (2, 4)
# 视图变维  数据共享, b变a变
print(a)
d = a.ravel()  #变成一维
print(d)
d[2] = 4;
print(a)
print('-----------------------')

# 复制变维
c = d.flatten()
d[0] = 99;
print(c)

# 就地变维
c.shape = (2, 4)
print(c)
c[0] = 9
c.resize((4, 2))
print(c)
