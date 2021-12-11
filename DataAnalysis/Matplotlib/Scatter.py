import numpy as np
import matplotlib.pyplot as mp

# 散点图
# mp.scatter(
#     x,          # x轴坐标数组
#     y,          # y轴坐标数组
#     marker='',  # 点型
#     s=10,       # 大小
#     color='',   # 颜色
#     edgecolor='', # 边缘颜色
#     facecolor='', # 填充色
#     zorder=''  # 图层序号
# )

# numpy.random提供了normal函数用于产生符合正态分布的随机数
n = 100
# 172 :  期望值
# 10 :   标准差
# n :    数字产生数量
x = np.random.normal(172, 20, n)
y = np.random.normal(60, 10, n)

# 绘制平面散点图
mp.figure('Scatter', facecolor='lightgray')
mp.title('scatter')

# 设置颜色数组
d = (y - 175) ** 2 + (x - 17) ** 2
mp.scatter(x, y, marker='o', s=70, label='persons', c=d, cmap='jet')  # 'jet'为颜色映射表
mp.legend()         # 标签
mp.show()