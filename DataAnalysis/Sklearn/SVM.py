import time
import joblib
from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def svm_deom():
    """
    SVM对点集分类
    :return:
    """
    x = [[0, 0], [1, 1]]
    y = [0, 1]

    estimator = svm.SVC()
    estimator.fit(x, y)
    pre = estimator.predict([[2, 2]])
    print(pre)
    return None

def n_components_analysis(n, x_train, y_train, x_val, y_val):
    # 记录开始时间
    start = time.time()
    # pca降维实现
    pca = PCA(n_components=n)
    print(f"特征降维, 传递的参数为: {n}.")
    pca.fit(x_train)
    # 在训练集和测试集上进行降维
    x_train_pca = pca.transform(x_train)
    x_val_pca = pca.transform(x_val)
    print(x_val_pca)
    print(x_val_pca[1])

    # 利用svc进行训练
    print(f"开始使用svm进行训练...")
    estimator = svm.SVC()
    estimator.fit(x_train_pca, y_train)

    # 获取accuracy结果
    accuracy = estimator.score(x_val_pca, y_val)

    # 记录结束时间
    end = time.time()
    print(f"准确率为: {accuracy}, 消耗时间: {int(end - start)}s.\n")

    return accuracy, estimator


def digital_recognitionBySVM():
    """
    SVM多分类实现对图片数字的识别
    :return:
    """
    # 1.获取数据
    train = pd.read_csv('../../DataSet/SVM_train.csv')
    train_image = train.iloc[:, 1:]
    train_label = train["label"].values
    # 查看具体图像
    # num_image = train_image.iloc[1, :].values.reshape(28, 28)
    # plt.imshow(num_image)
    # plt.axis("off") # 不显示坐标轴
    # plt.show()

    # 2.数据处理 - 归一化
    transfer = MinMaxScaler(feature_range=[0, 1])
    transfer.fit_transform(train_image)
    # 3.数据集划分
    x_train, x_val, y_train, y_val = train_test_split(train_image, train_label, random_state=17)

    # 4.特征降维和模型训练 - 多次使用pca降维, 确定最后的最优模型

    # 传递多个n_components, 寻找最优结果
    # n_s = np.linspace(0.75, 0.9, 3)
    # accuracys = []
    # for n in n_s:
    #     accuracy = n_components_analysis(n, x_train, y_train, x_val, y_val)
    #     accuracys.append(accuracy)
    # plt.plot(n_s, accuracys)
    # plt.xlabel('n')
    # plt.ylabel('accuracy')
    # plt.show()

    # 5.确定最优参数为0.825
    accuracy, estimator = n_components_analysis(0.825, x_train, y_train, x_val, y_val)
    # 6.保存模型
    joblib.dump(estimator, 'SVM_Model.pkl')

    return None

def test_SVM_Model():
    # 外部导入模型
    estimator = joblib.load('SVM_Model.pkl')

    test = pd.read_csv('../../DataSet/SVM_train.csv')
    test_image = test.iloc[:, 1:]

    # 数据降维
    pca = PCA(n_components=0.825)
    test_image_pca = pca.fit_transform(test_image)

    test_image_pca = test_image_pca[:100]
    # print([test_image_pca[0]])

    for i in range(len(test_image)):
        # 查看具体图像
        num_image = test_image.iloc[i, :].values.reshape(28, 28)
        plt.subplot(1, 2, 1)
        plt.imshow(num_image)
        plt.axis("off") # 不显示坐标轴
        plt.subplot(1, 2, 2)
        plt.text(
            0.5, 0.5,  # 文本中心点
            str(estimator.predict([test_image_pca[i]])[0]),  # 文本
            ha='center',  # 图框水平居中
            va='center',  # 垂直居中
            size=36,  # 文本字体
            alpha=0.6  # 透明度
        )
        # 去除刻度
        plt.xticks([])
        plt.yticks([])
        plt.show()
        # print(f"第{i + 1}次估计结果: {estimator.predict([test_image_pca[i]])[0]}")




if __name__ == "__main__":
    # svm_deom()
    # digital_recognitionBySVM()
    test_SVM_Model()