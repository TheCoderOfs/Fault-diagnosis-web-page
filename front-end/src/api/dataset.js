import request from '@/utils/request'

export function getList(params) {
  return request({
    url: 'http://localhost:5003/datasets',
    method: 'get',
    params
  })
}

export function getDataSetNames(params) {
  return request({
    url: 'http://localhost:5003/dataset/names',
    method: 'get',
    params
  })
}

