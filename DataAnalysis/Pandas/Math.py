import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

# 创建DF
d = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack'
                       'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
    'Age' : pd.Series([25, 26, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10])
}
df = pd.DataFrame(d)
# print(df)

# 算术运算
data = pd.DataFrame(np.random.normal(0, 1, (4, 3)), columns=['col1', 'col2', 'col3'])
# 加法
data['col1'] += 3
print(data)
print('-' * 45)

# 逻辑运算
print(data['col1'] > 3)
# 逻辑运算函数  query, isin
print(data.query("col1 > 1 & col2 < 0"))
print(data['col1'].isin([2.4, 21.3]))
print('-' * 45)

# data['col1'].plot(kind='bar')
# mp.show()



# 测试描述性统计函数
print(df.sum(), '->sum')
# print(df.sum(1), '->sum(1)')  # 括号内的参数决定轴向, 默认为0, 1表示水平方向
# print(df.mean(), '->mean')
print(df.max(), '->max')
print(df.count(), '->count')
print(df.describe(), '->describe')  # 打印所有信息


