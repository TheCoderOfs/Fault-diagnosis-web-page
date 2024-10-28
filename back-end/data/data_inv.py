import pandas as pd
import numpy as np

# 读入数据
data = pd.read_csv('traindataset.csv')
data.info()

# 6分类问题
print(np.unique(data['label']))

data = data.drop('sample_id', axis=1)

data = data.drop('label', axis=1)
means = data.mean(axis=0)
print('[', end='')
for m in means:
    print(str(m)+', ', end='')
print(']', end='')