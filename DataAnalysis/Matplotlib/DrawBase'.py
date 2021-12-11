import numpy as np
import matplotlib.pyplot as mp

# 绘制sin & cos图像
# 线性拆分1000个点
x = np.linspace(-np.pi, np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x) / 2

# linestyle: 线性 '-' '--' '-.' ':'
# linewidth: 线宽
    # 数字
# color: <关键字参数> 颜色
    # 英文颜色单词 或 常见单词首字母 或 #4955435 或 (1, 1, 1) 或 (1, 1, 1, 1)
# alpha: <关键字参数> 透明度 (0 - 1)
    # 浮点数值

mp.plot(x, sinx, linestyle='--', linewidth=2, color='orangered', alpha=0.8, label='sin(x)')
mp.plot(x, cosx, linestyle='-.', linewidth=2, color='dodgerblue', alpha=0.9, label='cos(x)/2')

# 设置坐标轴的范围
mp.xlim(-np.pi, np.pi)
mp.ylim(-np.pi, np.pi)

# 设置坐标刻度
x_val_list = [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]
# 设置坐标刻度文本
texts = ['Π', 'Π / 2', '0', 'Π / 2', 'Π']
mp.xticks(x_val_list, texts)
mp.yticks([-1.0, -0.5, 0.5, 1.0])

# 设置坐标轴
# # 获取当前坐标轴字典, {'left' : 左轴, 'right' : 右轴, 'bottom' : 下轴, 'top' : 上轴}
# ax = mp.gca()
# # 获取其中某个坐标轴
# axis = ax.spines['坐标轴名']
# # 设置坐标轴的位置. 该方法需要传入2个元素的元组作为参数
# # type: <str> 移动坐标轴轴的参照类型  一般为'data'(以数据的值作为移动参照值)
# # val: 参照值
# axis.set_position((type, val))
# # 设置坐标轴的颜色
# # color: <str> 颜色字符串
# axis.set_color(color)

ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# 特殊点
# xarray: <序列> 所有需要标注点的水平坐标组成的序列
# yarray: <序列> 所有需要标注点的垂直坐标组成的序列
xarray = [-np.pi / 2, np.pi / 2]
yarray = [1, 0]
mp.scatter(xarray, yarray,
           marker='s',       # 点型 ~ matplotlib.markers
           s=70,            # 大小
           # edgecolors='red',   # 边缘色
           # facecolor='red',    # 填充色
           color='red',
           label='smaple points', # 图列
           zorder=3         # 绘制图层编号 (编号越大, 图层越往上, 避免被覆盖)
)

# 备注(p18)


# 图例
mp.legend(loc='best')   # 默认最优位置, 在plot中添加label
mp.show()