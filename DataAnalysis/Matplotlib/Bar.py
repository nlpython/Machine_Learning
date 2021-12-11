import numpy as np
import matplotlib.pyplot as mp

# mp.bar(
#     x,              # 水平坐标数组
#     y,              # 柱状图高度数组
#     width=,         # 柱子的宽度
#     color='',       # 填充颜色
#     align='center', # 位置
#     bottom=,        # 底部起始位置 也可以用[]
#     label='',
#     alpha=
# )

apples = np.array([83, 94, 64, 68, 90, 103, 54, 75, 45, 56, 78, 34])
oranges = np.array([65, 24, 87, 90, 120, 87, 98, 83, 64, 68, 90, 103])

# 绘制柱状图
mp.figure('Bar', facecolor='lightgray')
mp.title('Bar Chart')
mp.grid(linestyle=':')
x = np.arange(apples.size)
mp.bar(x - 0.2, apples, 0.4, color='limegreen', label='Apples', align='center')
mp.bar(x + 0.2, oranges, 0.4, color='orangered', label='Oranges', align='center')
# 设置刻度
mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

mp.legend()
mp.tight_layout()
mp.show()
