import pandas as pd
dataset_train = pd.read_csv("traindataset.csv")
from tqdm import trange
# print(type(dataset_train))

# 删除id
dataset_train = dataset_train.drop('sample_id', axis=1)

#求平均值
Feature_average = {}
for item in dataset_train.keys()[:-1]:
    Feature_average[item] = dataset_train[item].mean()

# print(Feature_average)
# print(dataset_train)
# print(len(dataset_train))

#替换none值为均值
# count = -1

# for item in dataset_train.keys()[:-1]:
#     count += 1
#     print(count)
#     for index in range(len(dataset_train)):
#         if pd.isna(dataset_train[item][index]):
#             dataset_train.loc[index,[item]]=Feature_average[item]
#             # dataset_train[item][index] = Feature_average[item]

dataset_train = dataset_train.fillna(Feature_average)

#处理验证集
data_test = pd.read_csv('validateset.csv')
F_average = {}
data_test = data_test.drop('sample_id',axis=1)
for column in dataset_train.columns.values:
    F_average[column] = dataset_train[column].mean()
# print(F_average)
data_test = data_test.fillna(F_average)

#保存数据集
# dataset_train.to_csv("train_10000.csv",index = False)
# data_test.to_csv("test.csv",index = False)
# print(dataset_train)
