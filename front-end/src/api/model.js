import request from '@/utils/request'

export function getList(params) {
  return request({
    url: 'http://localhost:5003/models',
    method: 'get',
    params
  })
}

// 获取所有可用模型名字
export function getModelNames(params) {
  return request({
    url: 'http://localhost:5003/models/name',
    method: 'get',
    params
  })
}

// 提交训练请求
export function trainModel(data) {
  return request({
    url: 'http://localhost:5003/train',
    method: 'post',
    data,
    headers: {
      'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarynl6gT1BKdPWIejNq'
    }
  })
}

// 下载指定模型
export function downloadModel(mn) {
  return request({
    url: 'http://localhost:5003/download/model',
    method: 'get',
    params: {
      modelname: mn
    }
  })
}
