from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as mp
import numpy as np

# ax3d = mp.gca(projection = '3d')

# # 散点图
# ax3d.scatter(
#     x,              # x, y, z轴坐标数组
#     y,
#     z,
#     marker='',      # 点型
#     s=10,           # 大小
#     zorder='',
#     color='',
#     edgecolor='',
#     facecolor='',
#     c = v,          # 颜色值
#     cmap=''
# )

n = 1000
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)

# 绘制三维点阵
mp.figure('3D Scatter', facecolor='lightgray')
ax3d = mp.gca(projection='3d')
d = x ** 2 + y ** 2 + z ** 2
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
ax3d.scatter(x, y, z, s=70, marker='o', c = d, cmap='jet')
mp.tight_layout()
mp.show()

# 三维曲面
# ax3d.plot_surface(
#     x, y, z,
#     rstride=30,         # 行跨距 (每30个像素为一个整体)
#     cstride=30,         # 列跨距
#     cmap='jet'          # 颜色映射
# )

n = 1000
# 生成矩阵网格图
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

# 画图
mp.figure('3D Countour', facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.plot_surface(x, y, z, cstride=30, rstride=30, cmap='jet')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
mp.tight_layout()

mp.show()

# 三维线框图
ax3d = mp.gca(projection='3d')
ax3d.plot_wireframe(x, y, z, cstride=30, rstride=30, linewidth=1)
mp.tight_layout()
mp.show()

