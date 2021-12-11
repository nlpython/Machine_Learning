import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as mc
import scipy.integrate as si

# 积分
# 案例: 在[-5, 5]区间绘制二次函数y = 2x^2 + 3x + 4 的曲线

def f(x):
    return 2 * x ** 2 + 3 * x + 4

a, b = -5, 5
x1 = np.linspace(a, b, 1001)
y1 = f(x1)
mp.figure('Integral', facecolor='lightgray')
mp.title('Integral', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.vlines(-5, 0, f(-5), color='orangered')
mp.vlines(5, 0, f(5), color='orangered')
mp.fill_between(x1, 0, f(x1), f(x1) > 0, color='orangered', alpha=0.4)
mp.plot(x1, y1, linewidth=2.0, color='red')

# 自定义微元法计算定积分
n = 50
px = np.linspace(a, b, n + 1)
py = f(px)
area = 0
for i in range(n):
    area += (py[i] + py[i + 1]) / 2 * (b - a) / 50
print(area)

# 调用API  scipy.integrate模块中quad方法计算积分
area = si.quad(f, a, b)[0]  # 第一个值为积分值, 第二个为误差
print(area)

mp.show()


