import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt



# test = pd.read_csv('../data/test.csv')
# test_X, test_y   = test.iloc[:,:-1], test.label
test = pd.read_csv('../test/test_data_100.csv')
test_X = test.drop('sample_id', axis=1)

# 处理Nan
dict = {}
means = [63.74800329572281, 285239.5862211744, 1.132153555035695, 1.1777545993085679, 251.50164114651713, 11.553379494087599, 4.526707407194237, 86348423908.14302, 82388.38999595708, 530634553397276.8, 0.9864108666931025, 356.25715004148896, 361941.9606673107, 8.092454868001019, 7.739589784330728, 0.8780234767433831, 3592432505032.5845, 57700.57397113918, 310319.804011149, 18.820566944909, 1956.637094886643, 257984.9461789487, 0.1705410486902681, 361.44780623603936, 1.438835242007831, 147138.92061814634, 91240.6337554146, 6.215773279840293, 335.6816198936315, 0.6701516477621573, 6.155195186717805, 66.95147699159786, 43.932670354277114, 7.7949467564614805, 1.5588583736422215, 8.941336764857217, 1798982068460.938, 456746.812501582, 20.961095853193243, 184085193.9154341, 343674.0154939326, 209.35403699485704, 556589999.7341291, 204160.13314688473, 29.725658919632735, 0.6349894168006096, 20.064780493185992, 396486.1770221814, 110281070.09668085, 10.516766022994322, 1.3617862431148022, 894224364436200.0, 398008.89480038505, 1.1868038390697109, 284781.20581015927, 359791.83087489393, 8.311635959005306, 0.0, 19105.337116947343, 7.283798560062951, 72795834.95309302, 101595.39238428429, 0.9625015672003119, 294.12918914930884, 1114.6901748819068, 10.875015521191267, 3903657091260.3076, 105.7377448815806, 296810.20585806, 476798.80745233357, 170.1943855943847, 0.801565452121111, 1124376.3484490276, 1.3464298971720212, 1.6506852997959287, 439.53609480703767, 7.218126090210453, 0.0, 4477.300670166321, 1750655977180728.5, 0.8700638689201546, 20.73480081517472, 5107878161.948216, 0.7001359126510015, 21543993130552.137, 0.09240980692945136, 2153370484100.1528, 19287052189.985172, 17782.142557439325, 76715520.62163097, 427860.6981195966, 1936317508592.3945, 1115.9376834707168, 463153.89849442005, 3992532.022393154, 116.98188795337313, 152933.528721909, 6.717698799745909, 147171.92196823205, 239.5317445958645, 0.0, 85464777.15238635, 189.38953041521495, 1.3904934979937729, 1.4821613216699832, 8.319666111224398, 229.71809768122029]
for idx, column in enumerate(test_X.columns.values):
    dict[column] = means[idx]
test_X = test_X.fillna(dict)


bst = xgb.Booster(model_file='../model/XGBoost_2023_04_24_21_22_06.model')
dtest = xgb.DMatrix(data=test_X)
pred = bst.predict(dtest)

# cnt = 0
# for idx, p in enumerate(pred):
#     if p==test_y[idx]:
#         cnt+=1
# print("accuracy: ", cnt/len(test_y))
#
#
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


# 可视化演示的时候，可以考虑100条以下的推理，补充到100条数据，然后再LDA降维
# 补数据
n = len(test_X)
if n < 100:
    data = pd.read_csv('../data/preprocess_train_100.csv')
    data = data.drop('sample_id', axis=1)
    label = data['label'].tolist()
    data = data.drop('label', axis=1)
    data = data.sample(n=100-n, replace=False)
    test_X = pd.concat([test_X, data], ignore_index=True)
    pred = np.append(pred, label[n:100])


lda = LinearDiscriminantAnalysis(n_components=3)
X = lda.fit_transform(test_X, pred)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[0:n, 0], X[0:n, 1], X[0:n, 2], c=pred[0:n], s=20)     # 补充的点不画
ax.view_init(25, 125)
plt.show()



