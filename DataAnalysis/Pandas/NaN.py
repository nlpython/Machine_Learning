import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

data = pd.read_csv('./krkopt.csv', names=['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'res']).head(30)

# 判断是否存在NaN
print('是否存在NaN:', np.any(data.isnull()))
data1 = data.dropna(axis='rows')     # 默认按行删除
# print(data)
data2 = data.fillna(value=1, inplace=False)     # inplace表示就地修改数据
# print(data2)

# 平均值替换
data['y1'].fillna(value=data['y1'].mean(), inplace=True)
data['y2'].fillna(value=data['y2'].mean(), inplace=True)
data['y3'].fillna(value=data['y3'].mean(), inplace=True)

data['x1'].fillna(value='a', inplace=True)
data['x2'].fillna(value='b', inplace=True)
data['x3'].fillna(value='c', inplace=True)

print(data)
print('是否存在NaN:', np.any(data.isnull()))

# 将?作为缺失值处理
data.replace(to_replace='?', value=np.nan)


