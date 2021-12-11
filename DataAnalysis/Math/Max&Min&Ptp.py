import numpy as np

a = np.random.randint(10, 100, 9)
b = np.random.randint(10, 100, 9)
print(a)
print(b)
print('--------------------')

Max = np.max(a)
Min = np.min(a)
print('Max =', Max, ' Min =', Min)
print('--------------------')

# 返回最大最小值下标
index_Max = np.argmax(a)
index_Min = np.argmin(a)
print('argMax =', index_Max, ' argMin =', index_Min)
print('--------------------')

# 将两个同为数组中对应元素中最大/最小元素构成一个新的数组
new_Arr1 = np.maximum(a, b)
new_Arr2 = np.minimum(a, b)
print('Max -> ', new_Arr1)
print('Min -> ', new_Arr2)