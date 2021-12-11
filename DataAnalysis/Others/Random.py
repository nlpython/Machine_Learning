import numpy as np

# 二项分布(binomial)
# 产生size个随机数, 每个随机数来自n次尝试中的成功次数, 其中每次尝试成功的概率为p
# np.random.binomial(n, p, size)
a = np.random.binomial(10, 0.4, 10)
print(a, '->二项分布')
# 某人投篮命中率为0.3, 投10次, 进5个球的概率:
print(sum(np.random.binomial(10, 0.3, 200000) == 5) / 200000)

# 超几何分布
# 产生size个随机数, 每个随机数t为在总样本中随机抽取nsample个样本后
# 好样本的个数, 总样本由ngood个好样本和nbad个坏样本组成
# np.random.hypergeometic(ngood, nbad, nsample, size)
b = np.random.hypergeometric(2, 6, 3, 10)
print(b, '->超几何分布')

# 正态分布
# 产生size个随机数, 服从标准正态分布(期望 = 0, 标准差 = 1)
# np.random.normal(size)
# 产生size个随机数, 服从正态分布(期望 = 1, 标准差 = 10)
# np.random.normal(loc=1, scale=10, size)