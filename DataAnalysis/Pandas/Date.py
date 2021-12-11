import pandas as pd
import numpy as np

# pandas识别的日期字符串格式
dates = pd.Series(['2011', '2011-02', '2011-03-01',
                   '2011/04/01', '2011/05/01 01:01:01',
                   '01 Jun 2011'])
# to_datetime() 转换日期数据类型
dates = pd.to_datetime(dates)
print(dates, dates.dtype, type(dates))
print('-' * 30)
# datetime类型数据支持日期运算
delta = dates - pd.to_datetime('1970-01-05')
print(delta)
# 获取天数数值
print(delta.dt.days)
print('-' * 45)


# DateTimeIndex
# 通过指定周期和频率, 使用date.range()函数就可以创建日期序列.默认范围的频率是天

# 以日为频率
datelist = pd.date_range('2019/08/21', periods=5)  # 创建连续天的日期
print(datelist)
# 以月为频率
datelist = pd.date_range('2019/08/21', periods=5, freq='M') # freq='M' 表示频率为月
print(datelist)
# 年
datelist= pd.date_range('2019/08/23', periods=5, freq='Y')
print(datelist)
print('-' * 45)
# 生成工作日序列
dates = pd.bdate_range('2019-8-1', periods=7)
print(dates.values)
# 构建某个区间的时间序列
dates = pd.date_range('2017-01-08', '2017-01-15', freq='D')
print(dates)










