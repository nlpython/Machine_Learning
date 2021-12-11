import math
import numpy as np
from hmmlearn import hmm

def HMM_demo():
    """
    HMM
    :return:
    """
    # 1.设定隐藏状态的集合
    states = ['box_1', 'box_2', 'box_3']
    n_states = len(states)

    # 2.设定观察状态的集合
    observations = ['red', 'white']
    n_observations = len(observations)

    # 3.设定初始状态分布
    start_probability = np.array([0.2, 0.4, 0.4])

    # 4.设定状态转移概率分布矩阵
    transition_probability = np.array([
        [0.5, 0.2, 0.3],
        [0.3, 0.5, 0.2],
        [0.2, 0.3, 0.5]
    ])

    # 5.设定观测状态概率矩阵
    emission_probability = np.array([
        [0.5, 0.5],
        [0.4, 0.6],
        [0.7, 0.3]
    ])

    # 6.设定模型参数
    model = hmm.MultinomialHMM(n_components=n_states)
    model.startprob_ = start_probability            # 初始状态分布
    model.transmat_ = transition_probability        # 状态转移概率分布矩阵
    model.emissionprob_ = emission_probability      # 观测状态概率矩阵

    # 7.HMM
    seen = np.array([[0, 1, 0]]).T          # 0, 1代表observations中颜色对应的索引
    box = model.predict(seen)
    score = model.score(seen)      # 返回的是一个对数值
    score = math.exp(score)

    print('球的观测序列为:\n', ", ".join(map(lambda x: observations[x], seen.flatten())))
    print('最可能的隐藏序列:\n', ", ".join(map(lambda x: states[x], box)))
    print('该观测序列序列概率:', score)

    return None

if __name__ == "__main__":
    HMM_demo()