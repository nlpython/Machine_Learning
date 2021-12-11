import pandas as pd
import numpy as np
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split

def xgboost_demo():
    # 1、获取数据
    titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    x = titan[["pclass", "age", "sex"]]
    y = titan["survived"]

    # 缺失值需要处理，将特征当中有类别的这些特征进⾏字典特征抽取
    x['age'].fillna(x['age'].mean(), inplace=True)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)

    # 对于x转换成字典数据x.to_dict(orient="records")
    # [{"pclass": "1st", "age": 29.00, "sex": "female"}, {}]
    transfer = DictVectorizer(sparse=False)
    x_train = transfer.fit_transform(x_train.to_dict(orient="records"))
    x_test = transfer.fit_transform(x_test.to_dict(orient="records"))

    # 模型初步训练

    xg = XGBClassifier()
    xg.fit(x_train, y_train)
    xg.score(x_test, y_test)
    # 针对max_depth进⾏模型调优
    depth_range = range(10)
    score = []
    for i in depth_range:
        xg = XGBClassifier(eta=1, gamma=0, max_depth=i)
    xg.fit(x_train, y_train)
    s = xg.score(x_test, y_test)
    print(s)
    score.append(s)

    plt.plot(depth_range, score)
    plt.show()

    return None

if __name__ == "__main__":
    xgboost_demo()