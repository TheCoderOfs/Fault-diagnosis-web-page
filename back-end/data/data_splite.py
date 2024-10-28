import pandas as pd
import numpy as np

# 读入数据
data = pd.read_csv('traindataset.csv')

# 删除id
data = data.drop('sample_id', axis=1)



# # 用平均数补全nan和空值
# for column in data.columns.values:
#     print(column)
#     mean = data[column].mean()
#     for i in range(len(data)):
#         if pd.isna(data[column][i]):
#             data.loc[i, [column]] = mean
dict = {}
for column in data.columns.values:
    dict[column] = data[column].mean()
data = data.fillna(dict)



# 随机抽取20%作为验证集，剩下为训练集
shuffled_data = data.sample(frac=1, random_state=1) # 打乱数据
n = np.round(len(data)*0.8).astype(int)
print(n)
train = data[0:n]
test = data[n+1:]

# 保存到csv
# train.to_csv('train_10000.csv', index=False)
# test.to_csv('test.csv', index=False)




