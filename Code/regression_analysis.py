import numpy as np
import pandas as pd
import statsmodels.api as sm
import scipy
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg

def correlation_analysis(datas):
    datas = datas.iloc[:, :-2]
    columns = datas.columns
    standard_s2 = MinMaxScaler()  # 创建StandardScaler()实例
    datas = standard_s2.fit_transform(datas)  # 将DataFrame格式的数据按照每一个series分别标准化
    datas = pd.DataFrame(datas, columns=columns)  # 将标准化后的数据改成DataFrame格式
    #result_1 = datas.corr('pearson')
    result_2 = datas.corr('spearman')
    print(result_2)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    mask = np.zeros_like(round(datas.corr(method='spearman'), 3))
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style('white'):
        sns.heatmap(round(datas.corr(method='spearman'), 3), cmap="YlGnBu", annot=True, mask=mask)
    plt.show()
    print(result_2)
file = r'F:\code\confidence score-master\text_asp.xlsx'
data = pd.read_excel(file)
#correlation_analysis(data)
#data.columns = ['y', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
data.columns = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'y']
x = data.iloc[:, 0:8] #生成自变量
y = data['y'] #生成因变量


# x_1 = list(data['x9'])
#
# statistic, p_value = scipy.stats.mannwhitneyu(y_1, x_1)
# print("Kruskal-Wallis statistic:", statistic)
# print("p-value:", p_value)
# r1, p1 = scipy.stats.spearmanr(x_1, y_1)
# print('相关性系数为{0},显著性水平为{1}'.format(r1, p1))
model = sm.MNLogit(y, x) #生成模型
result = model.fit() #模型拟合
print(result.summary()) #模型描述
def looper(limit):
    cols = ['x1', 'x2', 'x3', 'x5', 'x6', 'x7', 'x8']
    for i in range(len(cols)):
        data1 = data[cols]
        x = sm.add_constant(data1) #生成自变量
        y = data['y'] #生成因变量
        model = sm.MNLogit(y, x) #生成模型
        result = model.fit() #模型拟合
        pvalues = result.pvalues #得到结果中所有P值
        pvalues.drop('const',inplace=True) #把const取得
        pmax = max(pvalues) #选出最大的P值
        if pmax>limit:
            ind = pvalues.idxmax() #找出最大P值的index
            cols.remove(ind) #把这个index从cols中删除
        else:
            return result

result = looper(0.05)
print(result.summary())

