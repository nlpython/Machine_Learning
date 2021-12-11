import numpy as np
import matplotlib.pyplot as mp

# 协方差, 用于评估两组数据的相关性; 值为正, 则为正相关, 值为负, 则为负相关;
# 绝对值越大, 相关性越强

a = np.random.randint(1, 30, 10)
b = np.random.randint(1, 30, 10)
# 平均值
ave_a = np.mean(a)
ave_b = np.mean(b)
# 离差
dev_a = a - ave_a
dev_b = b - ave_b
# 协方差
cov = np.mean(dev_a * dev_b)
print(cov)

# 相关矩阵
m = np.corrcoef(a, b)    # 返回一个矩阵

# 绘图
mp.plot(a, color='orangered', label='A')
mp.plot(b, color='dodgerblue', label='B')
mp.legend()
mp.show()


