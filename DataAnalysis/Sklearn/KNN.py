from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import joblib


def KNN_iris_girdSearch():
    """
    KNN算法(鸢尾花的类型预测)
    :return:
    """
    # 1.获取数据
    iris = load_iris()
    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=18)
    # 3.特征工程 - 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.KNN算法训练
    estimator = KNeighborsClassifier()

    # 加入网格搜索和交叉验证
    # 参数准备
    param_dict = {'n_neighbors': [1 ,3, 5, 7, 9, 11]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)
    estimator.fit(x_train, y_train)

    # 5.模型检验
    # 方法1: 直接和真实值比对
    y_predict= estimator.predict(x_test)
    print('y_predict:', y_predict)
    print('直接比对真实值和测试值:\n', y_test == y_predict)
    # 方法2: 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率: ', score)
    print('最佳参数:', estimator.best_params_)
    print('最佳结果:', estimator.best_score_)
    print('最佳估计器:', estimator.best_estimator_)
    print('交叉验证结果:', estimator.cv_results_)
    return None


def KNN_iris():
    """
    KNN算法(鸢尾花的类型预测)
    :return:
    """
    # 1.获取数据
    iris = load_iris()
    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
    # 3.特征工程 - 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.KNN算法训练
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)
    # 5.模型检验
    # 方法1: 直接和真实值比对
    y_predict= estimator.predict(x_test)
    print('y_predict:', y_predict)
    print('直接比对真实值和测试值:\n', y_test == y_predict)
    # 方法2: 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率: ', score)

    return None

def dump_demo():
    # 1.获取数据
    iris = load_iris()
    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
    # 3.特征工程 - 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.KNN算法训练
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)
    # 5.保存模型
    joblib.dump(estimator, 'KNN.pkl')

    return None

def load_demo():
    # 外部导入模型
    estimator = joblib.load('KNN.pkl')

    # 1.获取数据
    iris = load_iris()
    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
    # 3.特征工程 - 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 5.模型检验
    # 方法1: 直接和真实值比对
    y_predict= estimator.predict(x_test)
    print('y_predict:', y_predict)
    print('直接比对真实值和测试值:\n', y_test == y_predict)
    # 方法2: 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率: ', score)


    return None


if __name__ == "__main__":
    # KNN_iris()
    KNN_iris_girdSearch()
    # dump_demo()
    # load_demo()