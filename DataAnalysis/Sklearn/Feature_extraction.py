from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba

def dict_demo():
    """
    字典特征抽取
    :return:
    """
    data = [{'city': '北京', 'temperature': 37}, {'city': '上海', 'temperature': 31}, {'city': '深圳', 'temperature': 28}]
    # 1.实例化一个转换器类
    transfer = DictVectorizer(sparse=False)
    # 2.调用fit_transform()
    data_new = transfer.fit_transform(data)
    print('data_new:\n', data_new, sep='')
    print('特征名字:\n', transfer.feature_names_, sep='')

    return None

def count_demo():
    """
    文本特征抽取
    :return:
    """
    data = ["life is short, i like python", "life is too long, i dislike python", "life is beautiful"]
    # 1.实例化一个转换器类
    transfer = CountVectorizer(stop_words=['is', 'too'])
    # 2.调用fit_transform()
    data_new = transfer.fit_transform(data)
    print('data_new:\n', data_new, sep='')
    print('data_new:\n', data_new.toarray(), sep='')
    print('特征名字:\n', transfer.get_feature_names(), sep='')

def cut_word(text):
    """
    进行中文分词  "我爱北京天安门" -> "我 爱 北京 天安门"
    :param text:
    :return:
    """
    text = "".join(list(jieba.cut(text)))
    return text


def count_chinese_demo():
    """
    中文文本特征抽取, 自动分词
    :return:
    """
    data = ["今天很残酷，明天更残酷，后天很美好，但绝大多数人是死在明天晚上，所以每个人都不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们时在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解他。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    # 1.分词处理
    data_new = []
    for sent in data:
        data_new.append(cut_word(sent))
    # 2.实例化一个转换器类
    transfer = CountVectorizer()
    # 3.调用fit_transform()
    data_final = transfer.fit_transform(data_new)
    print('data_final:\n', data_final, sep='')
    print('特征名字:\n', transfer.get_feature_names(), sep='')

    return None

def tfidf_demo():
    """
    Tf-idf文本特征抽取
    :return:
    """
    data = ["life is short, i like python", "life is too long, i dislike python", "life is beautiful"]
    # 1.实例化一个转换器类
    transfer = TfidfVectorizer(stop_words=['is', 'too'])
    # 2.调用fit_transform()
    data_new = transfer.fit_transform(data)
    # print('data_new:\n', data_new, sep='')
    print('data_new:\n', data_new.toarray(), sep='')
    print('特征名字:\n', transfer.get_feature_names(), sep='')


if __name__ == "__main__":
    dict_demo()
    # count_demo()
    # count_chinese_demo()
    # tfidf_demo()