from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def RF_otto():
    # 1.数据导入
    data = pd.read_csv('./train.csv')
    # 2.数据处理
    # 随机欠采样获取相应数据
    x = data.iloc[:, 1:-1]
    y = data['target']
    rus = RandomUnderSampler(random_state=23)
    x_resampled, y_resampled = rus.fit_resample(x, y)
    print(x_resampled.shape)
    # 将标签值转换为数字
    le = LabelEncoder()
    y_resampled = le.fit_transform(y_resampled)
    print(y_resampled)
    # 3.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(x_resampled, y_resampled, random_state=14)

    # 4.模型训练
    rf = RandomForestClassifier()
    rf.fit(x_train, y_train)

    print(rf.score(x_test, y_test))





if __name__ == "__main__":
    RF_otto()
