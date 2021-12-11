# encoding=utf-8
import pandas as pd

data = pd.read_csv("C:\\Users\\86185\\Documents\\Tencent Files\\2994056734\\FileRecv\\shangzheng.csv")
# 去掉最后以一列
dataset = data.iloc[:, :-1]
# 按时间降序
data = dataset.sort_values(by='date', ascending=False, ignore_index=True)
# print(data)

# 转换成日期
data['date'] = pd.to_datetime(data['date'])
data = data.set_index('date') # 将date设置为index

july_data = data['2021-07']
print(july_data)
july_data = july_data.iloc[:, 2: 4]

print(july_data, '->July data')

print(dataset)
print('highest:')
print('date:', dataset.sort_values(by='volume', ascending=False, ignore_index=True).iloc[0]['date'], 'volume:', dataset.iloc[0]['volume'])
print('lowest:')
print('date:', dataset.sort_values(by='volume', ascending=False, ignore_index=True).iloc[-1]['date'], 'volume:', dataset.iloc[-1]['volume'])

print(dataset.query('volume > 100000000'))

print(len(dataset.query('close < open')))

week = dataset['date']
week = pd.to_datetime(week).dt.dayofweek+1
print(week)

dataset['date'] = week
count = [0 for _ in range(7)]
for i in range(len(dataset)):
    if dataset.iloc[i, 1] < dataset.iloc[i, 2]:
        count[dataset.iloc[i, 0]] += 1
print(count)


