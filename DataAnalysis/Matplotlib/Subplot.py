import numpy as np
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('SubplotTest', facecolor='lightgray')
# 矩阵式布局
for i in range(1, 10) :
    mp.subplot(3, 3, i)
    mp.text(
        0.5, 0.5,       # 文本中心点
        '1',            # 文本
        ha = 'center',  # 图框水平居中
        va = 'center',  # 垂直居中
        size = 36,      # 文本字体
        alpha = 0.6     # 透明度
    )
    # 去除刻度
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout()  # 紧凑布局
mp.show()

# 网格式布局 (支持单元格的合并)
mp.figure('Grid Layout', facecolor='lightgray')
# 调用GridSpec方法拆分网格式布局
# rows : 行数
# cols : 列数
# gs = mg.GridSpec(rows, cols)   拆分成3行3列
gs = mg.GridSpec(3, 3)
# 合并0行 0, 1列为一个子表图
mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, '1', ha='center', va='center', size = 36, alpha = 0.6)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
# 合并0, 1行, 2列为一个子表图
mp.subplot(gs[:2, 2])
mp.text(0.5, 0.5, '2', ha='center', va='center', size = 36, alpha = 0.6)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

# 自由式布局


mp.show()

