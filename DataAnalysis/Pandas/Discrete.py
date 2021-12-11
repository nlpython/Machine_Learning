import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

# 数据的离散化
data = pd.Series([165, 174, 160, 180, 159, 163, 192, 184], index=['No' + str(i+1) for i in range(8)])
# print(data)
# No1    165
# No2    174
# No3    160
# No4    180
# No5    159
# No6    163
# No7    192
# No8    184

# 分组
# 自动分组
sr = pd.qcut(data, 3)
print(sr)
# 自定义分组
bins = [150, 165, 180, 195]
sr = pd.cut(data, bins)
print(sr.value_counts)

# 转成one-hot编码
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
sr = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(sr)
print(df_with_dummy)


