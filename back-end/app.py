import datetime
import json
import os

from flask import *
import logging as rel_log
from datetime import timedelta
import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from flask_cors import CORS

from core.loadmodel import loadmodel_default, loadmodel
from core.predict import predict
from core.train import train

# 设置APP信息
app = Flask(__name__)
CORS(app, resources=r'/*')
app.secret_key = 'secret!'
# 解决中文乱码
app.config['JSON_AS_ASCII'] = False

# 配置上传文件类型及目录
UPLOAD_FOLDER = r'./uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['csv', 'xls', 'txt'])


# 设置日志级别
werkzeug_logger = rel_log.getLogger('werkzeug')
werkzeug_logger.setLevel(rel_log.ERROR)

# # 解决缓存刷新问题
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# 判断文件类型是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def helloworld():
    return redirect(url_for('static', filename='./index.html'))


# 获得所有的数据信息
@app.route('/datasets', methods=['GET'])
def get_dataset_info():
    floder_path = r"./uploads/train"
    filename = os.listdir(floder_path)
    items = []
    for fname in filename:
        path = floder_path + '/' + fname
        item = {}
        item['filename'] = fname
        item['filetype'] = os.path.splitext(path)[-1]
        item['filesize'] = os.path.getsize(path) / (1024 * 1024)
        item['filesize'] = round(item['filesize'], 2)
        item['createtime'] = datetime.datetime.fromtimestamp(int(os.path.getctime(path)))
        items.append(item)
    floder_path = r"./uploads/test"
    filename = os.listdir(floder_path)
    for fname in filename:
        path = floder_path + '/' + fname
        item = {}
        item['filename'] = fname
        item['filetype'] = os.path.splitext(path)[-1]
        item['filesize'] = os.path.getsize(path) / (1024 * 1024)
        item['filesize'] = round(item['filesize'], 2)
        item['createtime'] = datetime.datetime.fromtimestamp(int(os.path.getctime(path)))
        items.append(item)
    data = {}
    data['total'] = len(items)
    data['items'] = items
    response = {}
    response['code'] = 20000
    response['data'] = data
    return json.dumps(response)


# 获取数据名称
@app.route("/dataset/names", methods=['GET'])
def get_dataset_name():
    folder_path = r"./uploads/train"
    file_names = os.listdir(folder_path)
    items = []
    for fname in file_names:
        item = {}
        item['label'] = fname
        item['value'] = fname
        items.append(item)
    response = {}
    response['code'] = 20000
    response['options'] = items
    return json.dumps(response)


# 获取已有模型信息
@app.route("/models", methods=['GET'])
def get_model_info():
    floder_path = r"./model"
    filename = os.listdir(floder_path)
    items = []
    for fname in filename:
        path = floder_path + '/' + fname
        item = {}
        item['modelname'] = fname
        # item['modelsize'] = os.path.splitext(path)[-1]
        item['modelsize'] = os.path.getsize(path) / (1024 * 1024)
        item['modelsize'] = round(item['modelsize'], 2)
        # item['accuracy'] = os.path.splitext(path)[-1]
        # item['prescision'] = 0.964
        # item['recall'] = 0.972
        # item['F1'] = 0.967
        item['createtime'] = datetime.datetime.fromtimestamp(int(os.path.getctime(path)))
        items.append(item)

    data = {}
    data['total'] = len(items)
    data['items'] = items
    response = {}
    response['code'] = 20000
    response['data'] = data
    return json.dumps(response)


# 获取已有模型名字
@app.route("/models/name", methods=['GET'])
def get_dataset_n():
    folder_path = r"./model"
    file_names = os.listdir(folder_path)
    items = []
    for fname in file_names:
        item = {}
        item['label'] = fname
        item['value'] = fname
        items.append(item)
    response = {}
    response['code'] = 20000
    response['options'] = items
    return json.dumps(response)


# 上传数据
@app.route("/upload/train", methods=['GET', 'POST'])
def upload_train_file():
    files = request.files['file']
    Judge = request.form.get('NaN')
    if Judge == 'true':
        files.filename = "NaN_" + files.filename
        filepath = os.path.join(r'./uploads/train', files.filename)
        files.save(filepath)
    else:
        filepath = os.path.join(r'./uploads/train', files.filename)
        files.save(filepath)
    return jsonify({'code': 20000, 'message': "数据上传成功"})


# 训练模型
@app.route('/train', methods=['POST'])
def train_model():
    dataset = request.form.get('dataset')
    ALG = request.form.get('ALG')
    modelname = request.form.get('modelname')
    type1 = request.form.get('type1')
    type2 = request.form.get('type2')
    current_app.model, current_app.model_name = train(r"./uploads/train/" + dataset, ALG, modelname, type1, type2)
    return jsonify({'code': 20000, 'message': '训练成功'})


# 下载文件
@app.route("/download/model", methods=['GET'])
def download_file():
    modelname = request.args.get('modelname')
    filepath = './model/' + modelname
    if os.path.exists(filepath):
        # return jsonify({'code': 20000, 'message' : '开始下载模型'})
        return send_file(filepath)
        # , send_file(filepath)
    else:
        return jsonify({'code': 30000, 'message': '找不到该模型'})


# 预测
# 预测一条
@app.route('/pred/one', methods=['GET', 'POST'])
def upload_test_file():
    modelname = request.form.get('modelname')
    index1 = modelname.find('-')
    index2 = modelname.find('_')
    ALG = modelname[index1 + 1:index2]
    file = request.files['testfile']
    if file and allowed_file(file.filename):
        src_path = os.path.join(r'./uploads/test', file.filename)
        file.save(src_path)
        # if current_app.model_name != modelname:
        current_app.model, current_app.model_name = loadmodel(modelname, ALG)
        data = pd.read_csv(src_path)
        sample_id, pred, prob = predict(data, current_app.model, ALG)
        predinfo = {}
        predinfo['code'] = 20000
        predinfo['message'] = '预测成功'
        preds = {}
        for idx, sid in enumerate(sample_id):
            preds[str(sid)] = int(pred[idx])
        predinfo['res'] = preds
        # print(predinfo)
        return json.dumps(predinfo)
    return jsonify({'code': 30000, 'message': '上传文件类型不合法，请上传csv/xls/txt格式的文件'})


# 查询当前模型
@app.route('/get/currentmodel', methods=['GET'])
def get_current_model():
    return jsonify({'modelname': current_app.model_name})


# 预测数据
@app.route('/pred/muti', methods=['GET', 'POST'])
def pred_test_file():
    modelname = request.form.get('modelname')
    index1 = modelname.find('-')
    index2 = modelname.find('_')
    ALG = modelname[index1 + 1:index2]
    file = request.files['testfile']
    if file and allowed_file(file.filename):
        src_path = os.path.join(r'./uploads/test', file.filename)
        file.save(src_path)
        # if current_app.model_name != modelname:
        current_app.model, current_app.model_name = loadmodel(modelname, ALG)
        # print(current_app.model)
        # print(current_app.model_name)
        data = pd.read_csv(src_path)
        Feature_average = {}
        for item in data.keys()[1:]:
            Feature_average[item] = data[item].mean()
        data = data.fillna(Feature_average)
        sample_id, pred, prob = predict(data, current_app.model, ALG)
        predinfo = {}
        predinfo['code'] = 20000
        predinfo['message'] = '预测成功'
        preds = []
        for idx, sid in enumerate(sample_id):
            p = {}
            p['sid'] = str(sid)
            # print(pred[idx])
            p['label'] = int(pred[idx])
            p['confidence'] = float(prob[idx, pred[idx]])
            preds.append(p)
        predinfo['preds'] = preds

        # 可视化计算
        # 处理Nan
        MAXCOUNT = 100
        test_X = data
        # dict = {}
        # means = [0, 63.74800329572281, 285239.5862211744, 1.132153555035695, 1.1777545993085679, 251.50164114651713,
        #          11.553379494087599, 4.526707407194237, 86348423908.14302, 82388.38999595708, 530634553397276.8,
        #          0.9864108666931025, 356.25715004148896, 361941.9606673107, 8.092454868001019, 7.739589784330728,
        #          0.8780234767433831, 3592432505032.5845, 57700.57397113918, 310319.804011149, 18.820566944909,
        #          1956.637094886643, 257984.9461789487, 0.1705410486902681, 361.44780623603936, 1.438835242007831,
        #          147138.92061814634, 91240.6337554146, 6.215773279840293, 335.6816198936315, 0.6701516477621573,
        #          6.155195186717805, 66.95147699159786, 43.932670354277114, 7.7949467564614805, 1.5588583736422215,
        #          8.941336764857217, 1798982068460.938, 456746.812501582, 20.961095853193243, 184085193.9154341,
        #          343674.0154939326, 209.35403699485704, 556589999.7341291, 204160.13314688473, 29.725658919632735,
        #          0.6349894168006096, 20.064780493185992, 396486.1770221814, 110281070.09668085, 10.516766022994322,
        #          1.3617862431148022, 894224364436200.0, 398008.89480038505, 1.1868038390697109, 284781.20581015927,
        #          359791.83087489393, 8.311635959005306, 0.0, 19105.337116947343, 7.283798560062951, 72795834.95309302,
        #          101595.39238428429, 0.9625015672003119, 294.12918914930884, 1114.6901748819068, 10.875015521191267,
        #          3903657091260.3076, 105.7377448815806, 296810.20585806, 476798.80745233357, 170.1943855943847,
        #          0.801565452121111, 1124376.3484490276, 1.3464298971720212, 1.6506852997959287, 439.53609480703767,
        #          7.218126090210453, 0.0, 4477.300670166321, 1750655977180728.5, 0.8700638689201546, 20.73480081517472,
        #          5107878161.948216, 0.7001359126510015, 21543993130552.137, 0.09240980692945136, 2153370484100.1528,
        #          19287052189.985172, 17782.142557439325, 76715520.62163097, 427860.6981195966, 1936317508592.3945,
        #          1115.9376834707168, 463153.89849442005, 3992532.022393154, 116.98188795337313, 152933.528721909,
        #          6.717698799745909, 147171.92196823205, 239.5317445958645, 0.0, 85464777.15238635, 189.38953041521495,
        #          1.3904934979937729, 1.4821613216699832, 8.319666111224398, 229.71809768122029]
        #
        # for idx, column in enumerate(test_X.columns.values):
        #     if idx == 0:  # sample_id不补
        #         continue
        #     dict[column] = means[idx]
        # # test_X = test_X.fillna(dict)
        n = len(test_X)
        # if n < 100:  # n小于100补到100, 补在后面
        #     data = pd.read_csv('./data/preprocess_train_100.csv')
        #     data = data.sample(n=100 - n, replace=False)
        #     label = data['label'].tolist()
        #     data = data.drop('label', axis=1)
        #     test_X = pd.concat([test_X, data], ignore_index=True)
        #     pred = np.append(pred, label)
        if n > 100:  # n大于100，保留100个
            test_X = test_X.iloc[0:100]
            pred = pred[0:100]
            n = 100
        lda = LinearDiscriminantAnalysis(n_components=3)
        X = lda.fit_transform(test_X.iloc[:, 1:], pred)

        data = {}
        data['data0'] = []
        data['data1'] = []
        data['data2'] = []
        data['data3'] = []
        data['data4'] = []
        data['data5'] = []
        for idx in range(n):
            label = pred[idx]
            point = X[idx, :].tolist()
            point.append(0)
            point.append(int(test_X['sample_id'][idx]))
            data['data' + str(label)].append(point)

        predinfo['data'] = data
        # print(predinfo)
        return json.dumps(predinfo)
    return jsonify({'code': 30000, 'message': '上传文件类型不合法，请上传csv/xls/txt格式的文件'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=False)
