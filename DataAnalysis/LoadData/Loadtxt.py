import numpy as np
import matplotlib.pyplot as mp

# loadtxt
# data = np.loadtxt(
#     'C:/user/86153/t.csv',   # 文件地址
#     delimiter=',',           # 分隔符
#     skiprows=1,              # 跳过几行
#     encoding='utf-8',        # 解码方式
#     usecols=(1, 3, 4),       # 读取列标号
#     dtype='U10, f8, int32',  # 每列的数据类型
#     unpack=false,            # 是否拆包, 每列拆为一个数组
#     converters={3 : dmy2ymd) # 将第3列的数据由 日月年 转换为 年月日格式 (也可以自定义函数)
# )

age, weight = np.loadtxt(
    'C:\\Users\\86185\\PycharmProjects\\CODE_Python\\DataAnalysis\\LoadData\\dates.csv',
    delimiter=',',
    encoding='utf-8',
    usecols=(1, 2),
    dtype='f8, f8',
    unpack=True,
)

# 绘制年龄体重散点图
mp.figure('Age-Weight', facecolor='lightgray')
mp.title('Age-Weight')
mp.xlabel('age')
mp.ylabel('wgt')
mp.scatter(
    age,
    weight,
    s=70,
    color='red'
)
mp.tight_layout()
mp.show()