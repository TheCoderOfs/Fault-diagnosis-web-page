import pandas as pd
import numpy as np
import lightgbm as lgb

test = pd.read_csv('../data/test.csv')
test_X, test_y   = test.iloc[:,:-1], test.label


clf = lgb.Booster(model_file='../model/default.model')
prob = clf.predict(test_X)
pred = np.argmax(prob, axis=1)

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



