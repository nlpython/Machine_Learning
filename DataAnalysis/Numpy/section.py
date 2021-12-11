import numpy as np

a = np.arange(1, 10)
print('-----一维数组切片-----')
print(a)            # [1 2 3 4 5 6 7 8 9]
print(a[:3])        # [1 2 3]
print(a[3:6])       # [4 5 6]
print(a[6:])        # [7 8 9]
print(a[::-1])      # [9 8 7 6 5 4 3 2 1]
print(a[:-4:-1])    # [9 8 7]
print(a[-4:-7:-1])  # [6 5 4]
print(a[-7::-1])    # [3 2 1]
print(a[::], a[:])  # [1 2 3 4 5 6 7 8 9] [1 2 3 4 5 6 7 8 9]
print(a[::3])       # [1 4 7]
print(a[1::3])      # [2 5 8]

print('\n-----二维数组切片-----')
a.shape = (3, 3)
print(a)
print(a[0:2:1, :2])   # 取前两行前两列
print(a[::2, ::2])
