import numpy as py
import datetime as dt

# 转换器函数: 将日-月-年格式的日期字符串转换为星期
def dmy2wday (dmy):
    dmy = str(dmy)
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    wday = date.weekday()
    return wday

res = dmy2wday('17-4-2021')
print(res)
