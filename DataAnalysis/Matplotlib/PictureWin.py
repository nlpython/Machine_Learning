import numpy as np
import matplotlib.pyplot as mp

# 手动创建 matplotlib 窗口
mp.figure(
    'A Figure',         # 窗口标题栏文档
    figsize=(4, 3),     # 窗口大小 <元组>
    dpi=120,            # 像素密度
    facecolor='gray'    # 图表背景色
)
mp.figure('B figure', facecolor='lightgray')
# 设置图表标题 显示在图表上方
mp.title("Stock's price", fontsize=12)
# 设置水平轴文本
mp.xlabel('time', fontsize=12)
# 设置垂直轴文本
mp.ylabel('price', fontsize=12)
# 设置刻度参数
mp.tick_params(labelsize=8)
# 设置图标网格线  linestyle设置线的属性
    # - or solid  粗线
    # -- or dashed 虚线
    # -. or dashdot 点虚线
    # : or dotted 点线
mp.grid(linestyle='--')
mp.plot([1, 2, 3, 4, 5, 6], [2, 4, 5, 2, 1, 3])

mp.show()