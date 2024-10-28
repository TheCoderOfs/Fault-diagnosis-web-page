import lightgbm as lgb
import xgboost as xgb


def loadmodel_default():
    clf = lgb.Booster(model_file='./model/default.model')
    return clf, 'default.model'


def loadmodel(filename, ALG):
    path = "./model/"
    if ALG == 'lightGBM':
        clf = lgb.Booster(model_file=path + filename)
        return clf, filename
    else:
        bst = xgb.Booster(model_file=path + filename)
        return bst, filename
