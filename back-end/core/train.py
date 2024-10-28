import time

from core.loadmodel import loadmodel

import pandas as pd
import lightgbm as lgb
import xgboost as xgb


def train(datafile, ALG, name, type1, type2):
    # 数据处理
    data = pd.read_csv(datafile)
    data = data.drop('sample_id', axis=1)  # 删除sample_id列

    filename = ''
    if type1 == "true":
        Feature_average = {}
        for item in data.keys()[:]:
            Feature_average[item] = data[item].mean()
        data = data.fillna(Feature_average)

    if type2 == "true":
        Feature_average = {}
        for item in data.keys()[:]:
            Feature_average[item] = data[item].mean()
        data = data.fillna(Feature_average)

    train_X, train_y = data.iloc[:, :-1], data.label
    # 训练
    if ALG == 'lightGBM':
        clf = lgb.LGBMClassifier(max_depth=10, num_leaves=39, n_estimators=140, n_jobs=-1)
        clf.fit(train_X, train_y)
        # 保存模型
        path = "./model/"
        filename = time.strftime(f'{name}-{ALG}_%Y_%m_%d_%H_%M_%S.model', time.localtime())
        clf.booster_.save_model(path + filename)

    elif ALG == 'XGBoost':
        dtrain = xgb.DMatrix(data=train_X, label=train_y)
        params = {
            'max_depth': 8,
            'objective': 'multi:softmax',  # error evaluation for multiclass training
            'num_class': 6,
            # Set number of GPUs if available
            'n_gpus': 0
        }
        bst = xgb.train(params, dtrain)
        path = "./model/"
        filename = time.strftime(f'{name}-{ALG}_%Y_%m_%d_%H_%M_%S.model', time.localtime())
        bst.save_model(path + filename)

    # 返回模型
    return loadmodel(filename, ALG), filename
