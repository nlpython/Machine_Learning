import numpy as np

dates = ['2011-01-01', '2011', '2011-02',
         '2012-01-01', '2012-02-01 10:10:00']
date = np.array(dates)

date = date.astype('M8[D]')  #M8[s]  Y M D h m s
print(date, date.dtype)

# date减法
print(date[0] - date[2])