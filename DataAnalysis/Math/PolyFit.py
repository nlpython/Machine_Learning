import numpy as np
import matplotlib.pyplot as mp

# polyfit 多项式拟合
# polyval 多项式求值
# polyder(p) 多项式求导
# roots(p) 多项式求根
# polysub(p1, p2) 两个多项式函数的差函数的系数 (可通过求差函数的根求两个曲线的交点)

a = np.array([1, 2, 3, 4, 5, 6, 7, 8], 'float')
b = np.array([2.4, 5.7, 8.5, 2.1, 5.6, 9.0, 1.4, 4.5], 'float')

p = np.polyfit(a, b, 6)     # 多项式拟合
X = np.linspace(0, 9, 1000)
Y = np.polyval(p, X)
# 求导
Q = np.polyder(p)
xs = np.roots(Q)
ys = np.polyval(Q, xs)

# 绘图
mp.figure('PolyFit', facecolor='lightgray')
mp.title('Polyfit')
mp.scatter(
    a, b,
    color='red',
    s=20,
    alpha=0.8,
    label='real'
)
mp.plot(X, Y, color='dodgerblue', linewidth=1.2, label='fit')
mp.ylim(-3, 15)
mp.legend()
mp.tight_layout()
mp.show()

