import time

import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd

from sklearn.model_selection import train_test_split

# 读入训练集和测试集
train = pd.read_csv('../Data/train.csv')
test = pd.read_csv('../Data/test.csv')

# 将数据集的特征和标签分离
train_X, train_y = train.iloc[:,:-1], train.label
test_X, test_y   = test.iloc[:,:-1], test.label
dtrain = xgb.DMatrix(data=train_X, label=train_y)
dtest = xgb.DMatrix(data=test_X)



params = {
    'max_depth': 7,
    'objective': 'multi:softmax',  # error evaluation for multiclass training
    'num_class': 6,
    'seed':1000
}

bst = xgb.train(params, dtrain)
pred = bst.predict(dtest)

cnt = 0
for idx, p in enumerate(pred):
    if p == test_y[idx]:
        cnt += 1
accuracy = cnt/len(test_y)
print("accuracy: ", accuracy)


# TP = np.zeros([6])
# FP = np.zeros([6])
# TN = np.zeros([6])
# FN = np.zeros([6])
#
# for c in range(6):
#     for i in range(len(test_y)):
#         label = test_y[i]
#         if pred[i] == c and label == c:
#             TP[c] += 1
#         if pred[i] == c and label != c:
#             FP[c] += 1
#         if pred[i] != c and label != c:
#             TP[c] += 1
#         if pred[i] != c and label == c:
#             FN[c] += 1
#
# P = TP / (TP + FP)
# R = TP / (TP + FN)
# macro_P = np.sum(P)/6
# macro_R = np.sum(R)/6
# macro_F1 = 2*macro_P*macro_R/(macro_P+macro_R)
# print(P)
# print(R)
# print(macro_F1)

plot_importance(bst,max_num_features=10)
plt.show()
# path = "../model/"
# filename = time.strftime('XGBoost_%Y_%m_%d_%H_%M_%S.model', time.localtime())
# bst.save_model(path+filename+"_"+str(accuracy))



