from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, classification_report, roc_auc_score
import pandas as pd
import numpy as np

def getData():
    # 1.获取数据
    boston = load_boston()
    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=17)
    # 3.特征工程 - 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    return x_train, x_test, y_train, y_test

def linear_Boston1():
    """
    正规方程的优化方法对波士顿房价进行预测
    :return:
    """
    # 1-3.获取数据
    x_train, x_test, y_train, y_test = getData()

    # 4.预估器
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)

    # 5.得出模型
    print('正规方程权重系数为:', estimator.coef_)
    print('偏置为:', estimator.intercept_)

    # 6.均方误差
    y_predict = estimator.predict(x_test)
    error = mean_squared_error(y_test, y_predict)
    print('均方误差:', error)

    return None

def linear_Boston2():
    """
    梯度下降的优化方法对波士顿房价进行预测
    :return:
    """
    # 1-3.获取数据
    x_train, x_test, y_train, y_test = getData()
    # 4.预估器
    estimator = SGDRegressor()
    estimator.fit(x_train, y_train)

    # 5.得出模型
    print('梯度下降权重系数为:', estimator.coef_)
    print('偏置为:', estimator.intercept_)

    # 6.均方误差
    y_predict = estimator.predict(x_test)
    error = mean_squared_error(y_test, y_predict)
    print('均方误差:', error)

    return None

def ridge_Boston():
    """
    岭回归对波士顿房价进行预测
    :return:
    """
    # 1-3.获取数据
    x_train, x_test, y_train, y_test = getData()
    # 4.预估器
    estimator = Ridge()
    estimator.fit(x_train, y_train)

    # 5.得出模型
    print('岭回归权重系数为:', estimator.coef_)
    print('偏置为:', estimator.intercept_)

    # 6.均方误差
    y_predict = estimator.predict(x_test)
    error = mean_squared_error(y_test, y_predict)
    print('均方误差:', error)

    return None

def logisitc_cancer():
    """
    逻辑回归对癌症肿瘤 良/恶性 的预测
    :return:
    """
    # 1. 读取数据
    column_name = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                   'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                   'Normal Nucleoli', 'Mitoses', 'Class']
    path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
    data = pd.read_csv(path, names=column_name)
    # 2.缺失值处理 - 删除缺失样本
    data = data.replace(to_replace='?', value=np.nan)  # 将缺失值标记为 NaN
    data.dropna(inplace=True)
    # 3.划分数据集
    x = data.iloc[:, 1:-1]
    y = data["Class"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=17)
    # 4.特征工程 - 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 5.逻辑回归预估器
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)
    # 6.查看权重和偏置
    print('回归系数:', estimator.coef_)
    print('偏置:', estimator.intercept_)
    # 7.模型评估
    score = estimator.score(x_test, y_test)
    print('准确率: ', score)
    # 查看精确率, 召回率, F1-socre
    y_predict = estimator.predict(x_test)
    report = classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"])
    print('report:', report)
    # 将y_test转换为0, 1
    y_true = np.where(y_test > 3, 1, 0)
    AUC = roc_auc_score(y_true, y_predict)
    print('AUC:', AUC)

    return None




if __name__ == "__main__":
    # linear_Boston1()
    # linear_Boston2()
    # ridge_Boston()
    logisitc_cancer()