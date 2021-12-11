from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import jieba

def evaluate_analyze_bayes():
    """
    朴素贝叶斯对商品评论进行情感分析
    :return:
    """
    # 1.导入不带情感的停用词
    stopwords = []
    with open('./stopwords.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for word in lines:
            stopwords.append(word)
    stopwords = list(set(stopwords))    # 去重
    # 2.导入训练数据
    data = pd.read_csv('./feedback.csv', encoding='gbk')
    # 2.1 抽取出评论进行jieba分词
    content = data["内容"]
    content_list = []
    for tmp in content:
        seg_list = jieba.cut(tmp, cut_all=False)
        seg_str = " ".join(seg_list)
        content_list.append(seg_str)


    le = LabelEncoder()
    data["评价"] = le.fit_transform(data["评价"])

    # 4.划分测试集和训练集
    x_train, x_test, y_train, y_test = train_test_split(data["内容"], data["评价"], random_state=18)

    # 5.特征工程 - 文本特征抽取Tf-idf
    transfer = TfidfVectorizer(stop_words=stopwords)
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 6.预估器训练
    estimator = MultinomialNB(alpha=1.0)
    estimator.fit(x_train, y_train)
    # 7.模型评估
    # 方法1: 直接和真实值比对
    y_predict= estimator.predict(x_test)
    print('y_predict:', y_predict)
    print('直接比对真实值和测试值:\n', y_test == y_predict)
    # 方法2: 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率: ', score)

    return None


if __name__ == "__main__":
    evaluate_analyze_bayes()