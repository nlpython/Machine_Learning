import numpy as np

# 奇异值分解
M = np.mat('4 11 14; 8 7 -2')
print(M, '->M')
U, sv, V = np.linalg.svd(M, full_matrices=False)
print(U, '->U')
print(sv, '->sv')
print(V, '->V')
# U, V都是正交矩阵 U * U.T 等于ones(U.shape)
print(U * np.diag(sv) * V)
