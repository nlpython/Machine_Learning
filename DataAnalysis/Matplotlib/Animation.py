import matplotlib.animation as ma
import numpy as np
import matplotlib.pyplot as mp

# # 定义更新函数行为
# def update(number):
#     pass
# # 每隔10毫秒执行一次update更新函数, 作用于mp.gcf()当前窗口对象
# # mp.gcf(): 获取当前窗口
# # update:   更新函数
# # interval: 间隔时间 (单元: 毫秒)
# anim = ma.FuncAnimation(mp.gcf(), update, interval=10)
# mp.show()

# 案列: 随机生成各种颜色的100个气球, 让它们不断增大
# 自定义一种可以存放在ndarray里的类型, 用于保存一个球
ball_type = np.dtype([
    ('position', float, 2),      # 位置
    ('size', float, 1),          # 大小
    ('growth', float, 1),        # 生长速度
    ('color', float, 4)])        # 颜色 (红, 绿, 蓝和透明度)
# 随机生成100个点对象
n = 100
balls = np.zeros(100, dtype=ball_type)
balls['position'] = np.random.uniform(0, 1, (n, 2))
balls['size'] = np.random.uniform(40, 70, n)
balls['growth'] = np.random.uniform(10, 20, n)
balls['color'] = np.random.uniform(0, 1, (n, 4))

# 创建窗口
mp.figure('Animation', facecolor='lightgray')
mp.title('Animation', fontsize=14)
mp.xticks([])
mp.yticks([])
print(balls['position'])

sc = mp.scatter(
    balls['position'][:, 0],
    balls['position'][:, 1],
    s=balls['size'],
    color=balls['color'],
    alpha = 0.5
)

def update(number) :
    # 选择一个点
    index = number % 100
    # 重新修改index位置元素的属性
    balls['position'][index] = np.random.uniform(0, 1, (1, 2))  # uniform均匀分布, normal正态分布
    balls['size'][index] = np.random.uniform(50, 70, 1)
    balls['size'] += balls['growth']
    # 重新绘制界面
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])

# 动起来
anim = ma.FuncAnimation(mp.gcf(), update, interval=30)  # 不接收返回值的话程序会死掉

mp.show()
