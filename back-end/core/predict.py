import pandas as pd
import numpy as np
import xgboost as xgb

def predict(data, model,ALG):
    sample_id = np.asarray(data.iloc[:, 0])  # 取出sample_id
    data = data.drop('sample_id', axis=1)    # 删除sample_id列
    if ALG == 'XGBoost':
        data = xgb.DMatrix(data=data)
        pred = model.predict(data)
        pred = pred.astype(int)
        margins = model.predict(data, output_margin=True)
        # 将边际分数转换为类别的概率
        probabilities = 1 / (1 + np.exp(-margins))
        # print(pred)
        # probabilities = probabilities.tolist()
        # print(type(probabilities))
        # print(probabilities)
        return sample_id,pred,probabilities
    prob = model.predict(data)
    pred = np.argmax(prob, axis=1)
    # print(pred)
    return sample_id, pred, prob