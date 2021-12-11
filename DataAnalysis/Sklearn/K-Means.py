import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import silhouette_score, calinski_harabasz_score


def K_Means_demo():
    """
    K-Means聚类
    :return:
    """
    # 数据处理
    data = pd.read_csv('../../DataSet/variance_data.csv')
    data = data.iloc[:, 1:-2]
    transfer = VarianceThreshold(threshold=5)
    data_new = transfer.fit_transform(data)

    # 预估器流程
    estimator = KMeans(n_clusters=3)
    estimator.fit(data_new)
    data_pred = estimator.predict(data_new)

    # 模型评估
    sc = silhouette_score(data_new, data_pred)
    print(sc)

def K_means_blobs():
    # 创建数据
    x, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1, -1], [0, 0], [1, 1], [2, 2]], cluster_std=[0.4, 0.2, 0.2, 0.2], random_state=9)
    plt.scatter(x[:, 0], x[:, 1], marker='o')
    plt.show()

    # k-meansx训练及可视化
    y_pre = KMeans(n_clusters=4, random_state=9).fit_predict(x)

    plt.scatter(x[:, 0], x[:, 1], c=y_pre)
    plt.show()

    pre_score = calinski_harabasz_score(x, y_pre)
    print(pre_score)  # 此值越大越好
    sc = silhouette_score(x, y_pre)
    print(sc)

    return None

if __name__ == "__main__":
    # K_Means_demo()
    K_means_blobs()
