import numpy as np
import matplotlib.pyplot as plt
from sklearn.semi_supervised import LabelSpreading
from sklearn.datasets import make_circles

def labelspreading():
    """
    LabelSpreading半监督学习
    :return:
    """
    # 获取数据
    n_samples = 200
    x, y = make_circles(n_samples=n_samples, shuffle=False)

    # 原始点图
    outer, inner = 0, 1
    plt.figure(figsize=(7, 7))
    plt.scatter(x[y == outer, 0], x[y == outer, 1], color='navy',
                marker='s', lw=0, label='outer dot', s=20)
    plt.scatter(x[y == inner, 0], x[y == inner, 1], color='c',
                marker='s', lw=0, label='inner label', s=20)
    plt.legend()
    # plt.show()

    # 将除第一个和最后一个的点标记打乱, 记为-1
    labels = np.full(n_samples, -1)
    labels[0] = outer
    labels[-1] = inner
    plt.figure(figsize=(7, 7))
    plt.scatter(x[labels == outer, 0], x[labels == outer, 1], color='navy',
                marker='s', lw=0, label='outer dot', s=20)
    plt.scatter(x[labels == inner, 0], x[labels == inner, 1], color='c',
                marker='s', lw=0, label='inner label', s=20)
    plt.scatter(x[labels == -1, 0], x[labels == -1, 1], color='darkorange',
                marker='s', lw=0, label='unlabeled')
    plt.legend()
    plt.show()

    # Learn with LabelSpreading
    estimator = LabelSpreading(kernel='knn', alpha=0.8)
    estimator.fit(x, labels)

    out_labels = estimator.transduction_
    plt.figure(figsize=(7, 7))
    plt.scatter(x[out_labels == outer, 0], x[out_labels == outer, 1], color='navy',
                marker='s', lw=0, label='outer dot', s=20)
    plt.scatter(x[out_labels == inner, 0], x[out_labels == inner, 1], color='c',
                marker='s', lw=0, label='inner label', s=20)
    plt.scatter(x[out_labels == -1, 0], x[out_labels == -1, 1], color='darkorange',
                marker='s', lw=0, label='unlabeled')
    plt.legend()
    plt.show()


    return None


if __name__ == "__main__":
    labelspreading()