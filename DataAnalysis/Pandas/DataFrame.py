import pandas as pd
import numpy as np

# DataFrame
# DataFrame是一个类似于表格的数据类型, 可以理解为一个二维数组, 索引有
# columns=['Name', 'Age'], index=['first', 'second', 'thrid'],dtype=float
# columns表示列索引名称, index表示行索引
# 两个维度, 可更改. DataFrame具有以下特点:
# -潜在的列是不同的类型
# -大小可变
# -标记轴(行和列)
# -可以对行和列执行算术运算

# 创建一个空的DataFrame
print('DataFrame', '-' * 45)
df = pd.DataFrame()
print(df)
# 通过列表进行创建DataFrame
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'], index=['first', 'second', 'thrid'])
print(df)
print(df['Name']['first'], "->['Name']['first']")
# 通过字典列表创建DataFrame
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# data = {'Name' : ['Tom', 'Jack', 'Steve'], 'Age' : [28, 13, 53, 21]}
df = pd.DataFrame(data)
print(df)
print('columns', '-' * 45)

# 列的访问
# DataFrame的单列数据为一个Series. 根据DataFrame的定义可以
# 知晓DataFrame是一个带有标签的二维数组, 每个标签相当一个列名

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print(df['one'], "->df['one']")
print(df['one']['a'])
print(df[['one', 'two']])
print('-' * 45)

# 列添加
df['three'] = pd.Series([2, 3, 4, 5], index=['a', 'b', 'c', 'd']) # index=df.index
print(df)
# 列删除
del(df['one'])
df.pop('two')
print(df)
print('Rows', '-' * 45)


# 行访问
# 如果只是需要访问DataFrame某几行数据的实现方式采用数组的选取方式, 使用':'即可:
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df[2:4])
# loc方法
print(df.loc['b'])     # df['b']不能访问
print(df.loc[['a', 'b']], '->loc')
# iloc方法接受的必须是行索引或列索引的位置.
print(df.iloc[2])
print(df.iloc[[2, 3]], '->iloc')
print(df.iloc[1, 1])   # 返回第一行第二列的数据
print('行添加', '-' * 45)

# 行添加
df = pd.DataFrame([['zs', 12], ['ls', 4]], columns=['Name', 'Age'])
df2 = pd.DataFrame([['ww', 12], ['zl', 4]], columns=['Name', 'Age'])
df = df.append(df2)
print(df)
print(df.iloc[0][0])
print('行删除', '-' * 45)

# 行删除
df = df.drop(0)       # 删除所有标签为0的数据
print(df)
print('修改元素', '-' * 45)

# 修改元素
df = pd.DataFrame([['xx', 12], ['ls', 4]], columns=['Name', 'Age'])
df2 = pd.DataFrame([['ww', 12], ['zl', 4]], columns=['Name', 'Age'])
df = df.append(df2)
print(df, '->df')

df['Name'][1] = 'Tom'       # 先拿到'Name'一行的所有元素, 再修改所有标签为1的数据
print(df)
print(df.iloc[0]['Age'])


