from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

def minmax_demo():
    """
    归一化
    :return:
    """
    # 1.获取数据
    data = pd.read_csv('../../DataSet/processing_data.csv')
    data = data.iloc[:, :3]
    # 2.实例化MinMaxSclaer()
    transfer = MinMaxScaler(feature_range=[0, 1])   # 默认[0, 1]
    # 3.调用fit_transform()
    data_new = transfer.fit_transform(data)
    print('data_new:\n', data_new, sep='')

    return None

def stand_demo():
    """
    标准化
    :return:
    """
    # 1.获取数据
    data = pd.read_csv('../../DataSet/processing_data.csv')
    data = data.iloc[:, :3]
    # 2.实例化MinMaxSclaer()
    transfer = StandardScaler()   # 默认[0, 1]
    # 3.调用fit_transform()
    data_new = transfer.fit_transform(data)
    print('data_new:\n', data_new, sep='')

if __name__ == "__main__":
    # minmax_demo()
    stand_demo()