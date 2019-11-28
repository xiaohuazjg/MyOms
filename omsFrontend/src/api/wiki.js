import request from '@/utils/request'
import { apiuri } from '@/config'

// wikis
export function postWiki(data) {
  return request({
    url: apiuri.wikis,
    method: 'post',
    data
  })
}

export function getWiki(query, id) {
  return request({
    url: id ? apiuri.wikis + id + '/' : apiuri.wikis,
    method: 'get',
    params: query
  })
}

export function putWiki(id, data) {
  return request({
    url: apiuri.wikis + id + '/',
    method: 'put',
    data
  })
}

export function deleteWiki(id) {
  return request({
    url: apiuri.wikis + id + '/',
    method: 'delete'
  })
}

// opswikis
export function postOpsWiki(data) {
  return request({
    url: apiuri.opswikis,
    method: 'post',
    data
  })
}

export function getOpsWiki(query, id) {
  return request({
    url: id ? apiuri.opswikis + id + '/' : apiuri.opswikis,
    method: 'get',
    params: query
  })
}

export function putOpsWiki(id, data) {
  return request({
    url: apiuri.opswikis + id + '/',
    method: 'put',
    data
  })
}

export function deleteOpsWiki(id) {
  return request({
    url: apiuri.opswikis + id + '/',
    method: 'delete'
  })
}
