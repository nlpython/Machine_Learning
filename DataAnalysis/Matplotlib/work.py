import numpy as np
import matplotlib.pyplot as mp

x = np.array([0.1488, 0.1163, 0.0893, 0.0569, 0.0549, 0.0486, 0.0416])
y = np.array([1/50, 3/50, 5/50, 10/50, 11/50, 12/50, 13/50]);
mp.figure('Qusetion 4', facecolor='lightgray')
mp.scatter(
    x, y, label='True value',zorder=3
)
p = np.polyfit(x, y, 4)
X = np.linspace(0.0416, 0.1488, 1000)
Y = np.polyval(p, X)
mp.plot(X, Y, color='red', linewidth=1.5, label='Fitted curve')
mp.title('Proportion-Probability')
mp.grid(':')
mp.xlabel('Probability')
mp.ylabel('Proportion')
mp.legend()
mp.tight_layout()
mp.show()