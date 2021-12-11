import numpy as np
import matplotlib.pyplot as mp

# 热成像
# 以图形的方式显示矩阵及矩阵中值的大小

# 生成矩阵网格图
n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

# 绘制矩阵颜色图
mp.imshow(z, cmap='jet', origin='lower')  # origin决定y轴方向
# 使用颜色条显示热度值
mp.colorbar()

mp.show()