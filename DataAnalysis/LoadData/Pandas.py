import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./krkopt.csv', names=['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'res'])
print(df)