from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


def svm_chess():
    data = pd.read_csv('krkopt.data')
    # data = data.iloc[0:6000, :]
    # 值替换
    le = LabelEncoder()
    data['res'] = le.fit_transform(data['res'])
    data.loc[data['res'] != 0,'res'] = 1
    data.iloc[:, 0:-1] = data.iloc[:, 0:-1].replace(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [1, 2, 3, 4, 5, 6, 7, 8])
    # 归一化
    transfer = MinMaxScaler(feature_range=[0, 1])   # 默认[0, 1]
    data_new = transfer.fit_transform(data.iloc[:, 0:-1])
    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(data_new, data['res'], random_state=19,  train_size=0.7)

    # 开始训练
    estimator = svm.SVC(probability=True)
    estimator.fit(x_train, y_train)

    y_predict = estimator.predict(x_test)
    print('预测值与真实值对比:', y_test == y_predict)
    print('概率预测:', estimator.predict_proba(x_test))
    accuracy = estimator.score(x_test, y_test)
    print('准确率:', accuracy)

    return None


if __name__ == "__main__":
    svm_chess()