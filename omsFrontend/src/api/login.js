import request from '@/utils/request'
import { apiuri } from '@/config'

export function loginByUsername(data) {
  return request({
    url: apiuri.login,
    method: 'post',
    data
  })
}

export function getUserInfo(query) {
  return request({
    url: apiuri.users,
    method: 'get',
    params: query
  })
}

// router
export function getRouterInfo(query) {
  return request({
    url: apiuri.routerinfo,
    method: 'get',
    params: query
  })
}
