import numpy as np

weight = np.loadtxt(
    'C:\\Users\\86185\\PycharmProjects\\CODE_Python\\DataAnalysis\\LoadData\\dates.csv',
    delimiter=',',
    encoding='utf-8',
    usecols=(2,),
    dtype='f8',
    unpack=False
)

# 总体标准差
std = np.std(weight)
print(std)

# 样本标准差
sstd = np.std(weight, ddof=1)
print(sstd)