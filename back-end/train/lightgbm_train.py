import time

import numpy as np
import pandas as pd
import lightgbm as lgb

# 读入训练集和测试集
train = pd.read_csv('../data/train.csv')
test = pd.read_csv('../data/test.csv')

# 将数据集的特征和标签分离
train_X, train_y = train.iloc[:,:-1], train.label
test_X, test_y   = test.iloc[:,:-1], test.label

clf = lgb.LGBMClassifier(max_depth = 10, num_leaves = 39, n_estimators = 140, n_jobs=-1)
clf.fit(train_X, train_y)
pred = clf.predict(test_X)


cnt = 0
for idx, p in enumerate(pred):
    if p==test_y[idx]:
        cnt+=1
print("accuracy: ", cnt/len(test_y))


TP = np.zeros([6])
FP = np.zeros([6])
TN = np.zeros([6])
FN = np.zeros([6])

for c in range(6):
    for i in range(len(test_y)):
        label = test_y[i]
        if pred[i] == c and label == c:
            TP[c] += 1
        if pred[i] == c and label != c:
            FP[c] += 1
        if pred[i] != c and label != c:
            TP[c] += 1
        if pred[i] != c and label == c:
            FN[c] += 1

P = TP / (TP + FP)
R = TP / (TP + FN)
macro_P = np.sum(P)/6
macro_R = np.sum(R)/6
macro_F1 = 2*macro_P*macro_R/(macro_P+macro_R)
print(P)
print(R)
print(macro_F1)

# path = "../model/"
# filename = time.strftime('lightGBM_%Y_%m_%d_%H_%M_%S.model', time.localtime())
# clf.booster_.save_model(path+filename)


