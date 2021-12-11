import numpy as np
import matplotlib.pyplot as mp

# 颜色填充
# mp.fill_between(
#     x,              # x轴水平坐标
#     sin_x,          # 下边界曲线上点的垂直坐标
#     cos_x,          # 上边界曲线上点的垂直坐标
#     sin_x < cos_x,  # 填充条件, 为True时填充
#     color='',
#     alpha=0.2
# )

# 绘制案例
x = np.linspace(0, 8 * np.pi, 1000)
sin_x = np.sin(x)
cos_x = np.cos(x / 2) / 2

mp.figure('Fill', facecolor='lightgray')
mp.title('Fill', fontsize=18)
mp.grid(':')
mp.plot(x, sin_x, color='dodgerblue', label='sinx')
mp.plot(x, cos_x, color='orangered', label='cos(x/2)/2')

# 开始填充
mp.fill_between(x, sin_x, cos_x, sin_x > cos_x, color='dodgerblue', alpha=0.3)
mp.fill_between(x, sin_x, cos_x, sin_x < cos_x, color='orangered', alpha=0.3)

mp.legend()
mp.show()
