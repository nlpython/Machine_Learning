from typing import Any, Union

import numpy as np
import matplotlib.pyplot as mp

# 等高线图
# cntr = mp.contour(
#     x,                  # 网格坐标矩阵的x坐标 (2维数组)
#     y,                  # 网格坐标矩阵的y坐标 (2维数组)
#     z,                  # 网格坐标矩阵的z坐标 (2维数组)
#     8,                  # 把等高线绘制成8部分
#     colors='black',     # 等高线的颜色
#     linewidth = 0.5     # 线宽
# )
# mp.clabel(cntr, fmt='%.2f', inline_spacing=2, fontsize=8)
#                 标签输出格式   标签与线空白间隔

n = 1000
# 生成矩阵网格图
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
# 上述代码得到二维数组x, y直接组成坐标点矩阵
# z为每个坐标对应的高度值
# (模拟采集海拔高度)
mp.figure('Contour', facecolor='lightgray')
cntr = mp.contour(x, y, z, 8, colors='black', linewidth=0.3)
mp.grid(linestyle=':')
# 为等高线图添加高度标签
mp.clabel(cntr, fmt='%.2f', inline_spacing=2, fontsize=8)
# 为等高线填充颜色
mp.contourf(x, y, z, 8, camp = 'jet')  # camp取决与z的大小

mp.show()