import request from '@/utils/request'


// 预测多条
export function predMulti(data) {
  return request({
    url: 'http://localhost:5003/pred/muti',
    method: 'post',
    data,
    headers: {
      'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarynl6gT1BKdPWIejNq'
    }
  })
}


// 预测一条
export function predOne(data) {
  return request({
    url: 'http://localhost:5003/pred/one',
    method: 'post',
    data,
    headers: {
      'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarynl6gT1BKdPWIejNq'
    }
  })
}

