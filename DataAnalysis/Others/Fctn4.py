import numpy as np

# where
a = np.random.randint(0, 10, 7)
print(a, '->a')
c = np.where(a > 4)
print(c)
print(c[0])
print(c[0][0])