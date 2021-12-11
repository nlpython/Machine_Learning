import numpy as np

# np.msort(待排序数组)  默认升序
# 可用np.msort(arr)[::-1]实现降序

# 联合间接排序
# 该排序支持为待排序序列排序, 若待排序列值相同, 则利用参考序列作为
# 参考继续排序. 最终返回排序过后的有序索引序列
# indices = np.lexsort((次排序序列, 主排序序列))

names = np.array(['Huawei', 'Apple', 'Mi', 'Oppo', 'Vivo'])
prices = np.array([6888, 8888, 2999, 3999, 3999])
volumes = np.array([60, 110, 40, 50, 70])
# 先按价格排序, 若价格相同, 再按销售量倒序排序
indices = np.lexsort((-volumes, prices))   # '-'表示倒序
print(indices)
print(names[indices])
print('------------------')


# 插入排序
# 若有需要向有序数组中插入元素, 并使数组依然有序, 可使用searchsorted
# indices表示待插入序列中元素应插入位置的索引
# indices = np.searchsorted(有序序列, 待插序列)
# np.insert(被插序列, 位置序列, 待插序列)
a = np.array([0, 4, 5, 6, 8, 10])
b = np.array([1, 2, 7])
print(indices)
a = np.insert(a, indices, b)
print(a)



