import numpy as np
import matplotlib.pyplot as mp

mp.figure(figsize=(10,10))
k = 1
for i in range(40):
    if k == 5:
        k = 1
    s = f"YM{(int)(i / 4) + 1}_CJ{k % 5}"
    data = np.loadtxt(
        'C:\\Users\\86185\\Desktop\\datas.csv',
        delimiter=',',
        encoding='utf-8-sig',
        usecols=(i),
        dtype='f8',
        unpack=False
    )
    mp.boxplot(
        data,
        vert=False,           # 横竖转置
        positions=[i + 1],    # 控制位置
        labels=[s],
        widths=0.4,
        showfliers=False,     # 是否显示异常值
        patch_artist=True     # 填充颜色
    )
    print(data.size)
    y = np.ones(data.size)
    y = y * (i + 1)
    mp.scatter(
        data, y,
        marker='.',
        s=10,
        color='black'
        # c=data, cmap='jet'
    )
    k += 1
ax = mp.gca()
ax.grid(
    axis='x',
    linestyle='-',
    alpha=0.5
)
mp.title('Species-Minutes', fontsize=15)
mp.xlabel('minutes')
mp.ylabel('species')
mp.tight_layout
mp.show()


# mp.boxplot(
#     (data1, data2),
#     labels=['A', 'B'],
#     vert=False,
#     showmeans=True
# )
# mp.boxplot(
#     data1,
#     labels='C',
#     positions=[3],
#     vert=False
# )
# # mp.show()
#
#
# # mp.title("Box-plot Test")
# # mp.savefig("a.png")
# mp.show()