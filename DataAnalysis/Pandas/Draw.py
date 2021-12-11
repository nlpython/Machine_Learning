import numpy as np
import pandas as pd
import matplotlib.pyplot as mp

labels = ['股票_' + str(i + 1) for i in range(100)]
date = pd.date_range(start='20200818', periods=5, freq='B')
stocks = np.random.normal(0, 1, (100, 5))
stocks = pd.DataFrame(stocks, index=labels, columns=date)

stocks.plot(x='2020-08-18', y='2020-08-21', kind='scatter')
mp.show()