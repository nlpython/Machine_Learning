import pandas as pd
import numpy as np

# pandas分组
# -聚合  计算汇总统计
# -转换  执行一些特定于组的操作
# -过滤  再某些情况下丢弃数据

d = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack'
                       'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
    'Year' : pd.Series([2015, 2016, 2013, 2015, 2019, 2016, 2019, 2013, 2015, 2016, 2015]),
    'Points': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10])
}
df = pd.DataFrame(d)
print(df, '->df')
dfed = df.groupby('Year').groups
print(dfed)
# 通过循环打印
for year, group in df.groupby('Year'):
    print(year)
    print(group)
print('-' * 45)

# 获得一个分组细节(拿到2015年的所有数据)
grouped = df.groupby('Year')
print(grouped.get_group(2015))
print('-' * 45)


# 分组聚合
# 聚合函数为每个组返回聚合值.当创建了分组(groupby)对象, 就可以
# 对每个分组数据执行求和, 求标准差等操作
# 聚合每一年的评分
grouped = df.groupby('Year')
print(grouped['Points'].agg(np.mean))
print(grouped['Points'].agg([np.mean, np.max, np.min]))

# pandas数据表关联
# 默认通过相同的class_name进行合并
left = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy',
                     'Brian', 'Bran', 'Bryce', 'Betty'],
    'class_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
})
right = pd.DataFrame({
    'class_id': [1, 2, 3, 4],
    'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassD']
})
print('-' * 45)
print(left, '->left\n')
print(right, '->right\n')
# 合并两个DataFrame     how参数, right,left右左连接, outer全连接, inner内连接, on确定以那个数据作为连接
# rs = pd.merge(left, right, on='subject_id', how='right')
rs = pd.merge(left, right, how='inner')
print(rs)

# pandas透视表与交叉表

