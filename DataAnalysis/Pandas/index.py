import pandas as pd
import numpy as np

stocks = np.random.normal(0, 1, (8, 7))
stocks_frame = pd.DataFrame(stocks)
# print(stocks_frame)

# 添加索引
labels = ['股票' + str(i + 1) for i in range(8)]
date = pd.date_range(start='20200818', periods=7, freq='B')
stocks_new = pd.DataFrame(stocks, index=labels, columns=date)
# print(stocks_new)
# print('index:', stocks_new.index)
# print('columns:', stocks_new.columns)

# 修改行列索引值
stocks_new.index = ['房价' + str(i + 1) for i in range(8)]      # 只能整体替换, 不能单独改变某个索引
# print(stocks_new)

# 将某一列设置为索引
dict = {'month': [2, 3, 4], 'sale': [98, 53, 12], 'percent': [0.2, 0.5, 0.3]}
data = pd.DataFrame(dict)
print(data)
# 将月份设置为索引
data = data.set_index('month')
print(data)
print('-' * 45)

# 索引取值
# 去掉某些列
stocks_new = stocks_new.drop(['2020-08-18', '2020-08-20', '2020-08-21'], axis=1)
print(stocks_new)
print(stocks_new[['2020-08-19', '2020-08-26']])
print('直接索引:', stocks_new['2020-08-19']['房价1'])     # 先列后行
print('loc按名字索引:', stocks_new.loc['房价2', '2020-08-26'])   # 先行后列
print('iloc按数字索引:', stocks_new.iloc[1, 2])  # 先行后列
