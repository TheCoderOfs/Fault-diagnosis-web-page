import pandas as pd
import xgboost as xgb
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from tqdm import tqdm
import time
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data_test = pd.read_csv("../Data/test.csv")
print("--------数据加载成功--------")
time.sleep(3)
test_X, test_y = data_test.iloc[:,:-1], data_test.label
bst = xgb.Booster(model_file='../model/XGBoost_2023_10_16_22_54_58.model_0.832')
time.sleep(3)
print("--------模型加载成功--------")
dtest = xgb.DMatrix(data=test_X)
pred = bst.predict(dtest)
length = len(pred)
# print(type(pred))
cnt = 0
# for idx, p in enumerate(pred):
#     if p == test_y[idx]:
#         cnt += 1
print("--------开始预测--------")
temp = 0
for i in tqdm(pred):
    if i == test_y[temp]:
        cnt += 1
    temp += 1
    time.sleep(0.005)
print("accuracy: ", cnt/len(test_y))
print("--------预测成功--------")
data_pred = data_test
pred = pd.DataFrame(pred,columns=['label'])
data_pred.label = pred
labels = np.asarray(data_pred.iloc[:, -1])
df = data_pred.drop('label', axis=1)

lda = LinearDiscriminantAnalysis(n_components=3)
X = lda.fit_transform(df, labels)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')#
ax.scatter(X[:, 0], X[:, 1],X[:,2], c=labels, s=20)
ax.view_init(30, 185)
plt.show()
# print(data_pred.iloc[:,-1])
# print(data_pred)
