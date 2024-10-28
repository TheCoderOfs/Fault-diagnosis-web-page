import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


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


lda = LinearDiscriminantAnalysis(n_components=3)
X = lda.fit_transform(df, labels)

# X = TSNE(n_components=3).fit_transform(df, labels)
# X = PCA(n_components=3).fit_transform(df, labels)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels, s=20)
ax.view_init(30, 185)
plt.show()