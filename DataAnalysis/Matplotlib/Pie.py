import numpy as np
import matplotlib.pyplot as mp

# 饼状图
# mp.pie(
#     values,             # 值列表
#     spaces,             # 扇形之间的间距列表
#     labels=[],          # 标签列表
#     colors=[],          # 颜色列表
#     '%dd%%',            # 标签所占比例格式
#     shadow=True,        # 是否显示阴影
#     startangle=90,      # 逆时针绘制饼状图时的起始角度
#     radius=1            # 半径
# )

mp.figure('Pie', facecolor='lightgray')
# 整理数据
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript', 'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered', 'limegreen', 'violet', 'gold']
mp.title('Pie', fontsize = 20)
# x, y轴等比例
mp.axis('equal')
mp.pie(values, spaces, labels, colors, '%.1f%%', shadow=True)
mp.tight_layout();
mp.show()
