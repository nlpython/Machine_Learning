import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

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
    r1 = pearsonr(data["pe_ratio"], data["pb_ratio"])
    print('相关系数:\n', r1, sep='')
    # 描绘revenue-total_expense散点图
    plt.scatter(data["revenue"], data["total_expense"])
    plt.xlabel("revenue"); plt.ylabel("total_expense")
    plt.show()
    r2 = pearsonr(data["revenue"], data["total_expense"])
    print('相关系数:\n', r2, sep='')

    return None

def PCA_demo():
    """
    PCA降维(主成分分析)
    :return:
    """
    data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]
    transfer = PCA(n_components=0.90)

    data_new = transfer.fit_transform(data)
    print('data_new:\n', data_new, sep='')


if __name__ == "__main__":
    variance_demo()
    # PCA_demo()