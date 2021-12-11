import numpy as np
import matplotlib.pyplot as mp

mp.figure('Locator', facecolor='lightgray')
x = np.linspace(-np.pi, np.pi, 1000)
y = np.sin(x) * 2
mp.plot(x, y, linestyle='-.', color='red', label='2sin(x)')
# 获取当前坐标轴
ax = mp.gca()
# 设置水平坐标轴的主刻度定位器
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
# 设置水平坐标轴的次刻度定位器 (间隔为0.1)
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.5))

# 空定位器: 不绘制刻度
# mp.NullLocator()
# 最大值定位器:
# 最多绘制nbins + 1个刻度
# mp.MaxNLocator(nbins=3)
# 定点定位器: 根据locs参数中的位置绘制刻度
# mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])
# 自动定位器: 由系统自动选择刻度的绘制位置
# mp.AutoLocator()
# 索引定位器: 由offset确定起始刻度, 由base确定相邻刻度的间隔
# mp.IndexLocator(offset=0.5, base=1.5)
# 多点定位器: 从0开始, 按照指定参数的间隔(缺省1)绘制刻度
# mp.MultipleLocator(num)
# 线性定位器: 等分numticks - 1份, 绘制numticks个刻度
# mp.LinearLocator(numticks=21)
# 对数定位器: 以base为底, 绘制刻度
# mp.LogLocator(base=2)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
mp.xticks([])
mp.yticks([])
# 设置坐标轴的范围
mp.xlim(-np.pi, np.pi)
mp.ylim(-np.pi, np.pi)
mp.show()

# # 刻度网格线
# ax = mp.gca();
# # 绘制网格线
# ax.grid(
#     which='',          # 'major'/'minor'/'both' <-> '主刻度'/'次刻度'
#     axis='',           # 'x'/'y'/'both' <-> 绘制x或y轴
#     linewidth=1,       # 线宽
#     linestyle='-',     # 线型
#     color='',          # 颜色
#     alpha=0.5          # 透明度
# )

# 绘制曲线[1, 10, 100, 1000, 100, 10, 1], 然后设置刻度网格线, 测试刻度网格线的参数
y = np.array([1, 10, 100, 1000, 100, 10, 1])
mp.figure('Normal & Log', facecolor='lightgray')
mp.subplot(211)
mp.title('Nomal', fontsize=20)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
ax.grid(which='major', axis='both', color='orangered', linewidth=0.5, alpha=0.5)
# ax.grid()
mp.plot(y, color='dodgerblue', linestyle='-')

mp.subplot(212)
# 半对数坐标
mp.semilogy(y)
mp.title('Log', fontsize=20)
mp.tight_layout()
mp.plot(y, color='dodgerblue', linestyle='-')

mp.show()



mp.figure('Locators', facecolor='lightgray')
locators = ['mp.NullLocator()',
            'mp.MaxNLocator(nbins=4)',
            'mp.FixedLocator([3, 6, 9])',
            'mp.AutoLocator()']
for i, locator in enumerate(locators):
    mp.subplot(len(locators), 1, i + 1)
    ax = mp.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0.5))
    ax.spines['left'].set_color('none')
    mp.yticks([])
    loc = eval(locator)
    print(loc)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
    mp.xlim(0, 10)
    mp.tight_layout()



mp.show()
