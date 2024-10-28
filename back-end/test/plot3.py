import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图

df = pd.read_csv('./train_data_500.csv')

# 删除id和标签
df = df.drop('sample_id', axis=1)
labels = np.asarray(df.iloc[:, -1])
df = df.drop('label', axis=1)

# 处理nan值
dict = {}
for column in df.columns.values:
    dict[column] = df[column].mean()
df = df.fillna(dict)

X_tsne = TSNE(n_components=2, random_state=11).fit_transform(df)
X_pca = PCA(n_components=2).fit_transform(df)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=labels, s=60)

plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, s=60)
plt.show()
