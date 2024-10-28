#xgboost 分类

import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd

# read in the iris data
# iris = load_iris()
dataset = pd.read_csv("E:\\VSCODEpython\\创新项目\\train.csv")
X,y= dataset.iloc[:,:-1],dataset.label

dtrain = xgb.DMatrix(data=X, label=y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234565)
y_test = y_test.tolist()
params = {
    'max_depth': 8,
    'objective': 'multi:softmax',  # error evaluation for multiclass training
    'num_class': 6,
    # Set number of GPUs if available
    'n_gpus': 0
}

plst = list(params.items())


dtrain = xgb.DMatrix(X_train, y_train)
model = xgb.train(plst, dtrain)

# 对测试集进行预测
dtest = xgb.DMatrix(X_test)
ans = model.predict(dtest)

# 计算准确率
cnt = 0
for idx, p in enumerate(ans):
    if p == y_test[idx]:
        cnt += 1
print("accuracy: ", cnt/len(y_test))

# 显示重要特征
plot_importance(model)
plt.show()
