from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def datasets_demo():
    """
    sklearn数据集的使用
    :return:
    """
    # 获取鸢尾花数据集
    iris = load_iris()
    # print("鸢尾花数据集的返回值: \n", iris)
    # # 返回值是一个继承自字典的Bench
    # print("数据集的描述\n", iris["DESCR"])
    # print("鸢尾花的特征值:\n", iris["data"])
    # print("鸢尾花的目标值:\n", iris.target)
    # print("鸢尾花特征值的名字:\n", iris.feature_names)
    # print("鸢尾花目标值的名字:\n", iris.target_names)

    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22) # test_size默认0.25
    print(x_train, x_test, y_train, y_test, sep='\n')

    return None

if __name__ == "__main__":
    # sklearn数据集的使用
    datasets_demo()





