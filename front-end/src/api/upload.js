import request from '@/utils/request'


// 上传训练数据集
export function uploadTrainDataSet(data) {
  return request({
    url: 'http://localhost:5003/upload/train',
    method: 'post',
    data,
    headers: {
      'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarynl6gT1BKdPWIejNq'
    }
  })
}
