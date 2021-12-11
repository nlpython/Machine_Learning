import numpy as np

# 已知n阶方阵A, 求特征值与特征数组
# eigvals :  特征值数组
# eigvecs :  特征向量数组
# eigvals, eigvecs = np.linalg.eig(A)
# 已知特征值和特征向量, 求方阵
# S = eigvecs * np.mat(np.diag(eigvals)) * eigvecs.I

A = np.mat('3 -2; 1 0')
print(A)
# 提取特征值
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)
# 求原方阵
S = eigvecs * np.mat(np.diag(eigvals)) * eigvecs.I
print(S)

# 抹掉一部分特征值
eigvals[-1] = 0
S1 = eigvecs * np.mat(np.diag(eigvals)) * eigvecs.I
print(S1)