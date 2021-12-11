import numpy as np

data = [
    ('zs', [90, 80, 85], 15),
    ('ls', [92, 81, 83], 16),
    ('ww', [95, 85, 95], 15)
]
# 第一种dtype
a = np.array(data, dtype='U3, 3int32, int32')
print(a)
print(a[0][1])
print('------------------------------')

# 更好的dtype设置方式
# b = np.array(data, dtype=[('name', 'U2', 2),
#                           ('score', 'int32', 3),
#                           ('age', 'int32', 1)])
# print(b)
# print(b[2]['age'], b[0]['score'])
# print('------------------------------')

# 第三种
c = np.array(data, dtype={'names': ['name', 'scores', 'age'],
                          'formats': ['U3', '3int32', 'int32']})
print(c[0]['name'])
print(c.itemsize)
print(c['name'])
