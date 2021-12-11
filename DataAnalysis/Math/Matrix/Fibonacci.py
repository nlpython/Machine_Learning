import numpy as np

# 输出斐波那契数列
n = 32
F = np.mat('1 1; 1 0')
for i in range(n):
    print((F**i)[0, 0])