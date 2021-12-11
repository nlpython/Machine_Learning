from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier

def decision_tree_iris():
    """
    用决策树对鸢尾花进行分类
    :return:
    """
    # 1.获取数据集
    iris = load_iris()
    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=8)

    # 3.使用决策树预估器
    # 加入网格搜索和交叉验证
    # 参数准备
    param_dict = {'max_depth': [x for x in range(2, 15)]}
    estimator = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=None)
    # 网格搜索
    # estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)

    estimator.fit(x_train, y_train)

    # 4.模型评估
    # 方法1: 直接和真实值比对
    y_predict = estimator.predict(x_test)
    print('y_predict:', y_predict)
    print('直接比对真实值和测试值:\n', y_test == y_predict)
    # 方法2: 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率: ', score)

    # 5.可视化决策树
    export_graphviz(estimator, out_file='./tree.dot', feature_names=iris.feature_names)

    return None


def random_forest_iris():
    """
    随机森林泰坦尼克号乘客生存分析
    :return:
    """
    # 1.获取数据
    iris = load_iris()
    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=8)
    # 3.使用随机森林预估器
    estimator = RandomForestClassifier(n_estimators=10, criterion='gini', max_depth=10, bootstrap=True,
                                       random_state=8, min_samples_split=2)
    estimator.fit(x_train, y_train)
    # 4.模型评估
    # 方法1: 直接和真实值比对
    y_predict = estimator.predict(x_test)
    print('y_predict:', y_predict)
    print('直接比对真实值和测试值:\n', y_test == y_predict)
    # 方法2: 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率: ', score)

    return None


if __name__ == "__main__":
    decision_tree_iris()
    # random_forest_iris()
