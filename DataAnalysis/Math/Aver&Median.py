import numpy as np

# 算术平均值
weight = np.loadtxt(
    'C:\\Users\\86185\\PycharmProjects\\CODE_Python\\DataAnalysis\\LoadData\\dates.csv',
    delimiter=',',
    encoding='utf-8',
    usecols=(2,),
    dtype='f8',
    unpack=False
)

print(weight.mean())
print(np.mean(weight))


# 加权平均值
s = [1, 2, 3, 4, 5]     # 数值
w = [4, 3, 2, 8, 1]     # 权重

print(np.average(s, weights=w))
print('-------------------------')

# 中位数
med = np.median(weight)
print(med)
print(np.sort(weight))

