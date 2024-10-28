import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # 空间三维画图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./train_data_100.csv')

# 删除id和标签
df = df.drop('sample_id', axis=1)
labels = np.asarray(df.iloc[:, -1])
df = df.drop('label', axis=1)

# 处理nan值
dict = {}
for column in df.columns.values:
    dict[column] = df[column].mean()
df = df.fillna(dict)

X_tsne = TSNE(n_components=3, random_state=11).fit_transform(df)
X_pca = PCA(n_components=3).fit_transform(df)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=labels, s=60)

ax.scatter(X_tsne[:, 0], X_tsne[:, 1], X_tsne[:, 2], c=labels, s=60)
ax.view_init(30, 185)
plt.show()