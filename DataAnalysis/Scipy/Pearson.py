import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from scipy.stats import pearsonr

def variance_demo():
    """
    特征降维
    :return:
    """
    data = pd.read_csv('../../DataSet/variance_data.csv')
    data = data.iloc[:, 1:-2]
    transfer = VarianceThreshold(threshold=5)
    data_new = transfer.fit_transform(data)
    print('data_new:\n', data_new, sep='')
    print(data_new.shape)
    # 计算相关系数
    r = pearsonr(data["pe_ratio"], data["pb_ratio"])
    print('相关系数:\n', r, sep='')

    return None


if __name__ == "__main__":
    variance_demo()