import request from '@/utils/request'
import { apiuri } from '@/config'

// hosts
export function postHost(data) {
  return request({
    url: apiuri.hosts,
    method: 'post',
    data
  })
}

export function getHost(query) {
  return request({
    url: apiuri.hosts,
    method: 'get',
    params: query
  })
}

export function putHost(id, data) {
  return request({
    url: apiuri.hosts + id + '/',
    method: 'put',
    data
  })
}

export function patchHost(id, data) {
  return request({
    url: apiuri.hosts + id + '/',
    method: 'patch',
    data
  })
}

export function deleteHost(id) {
  return request({
    url: apiuri.hosts + id + '/',
    method: 'delete'
  })
}

// idcs
export function postIdc(data) {
  return request({
    url: apiuri.idcs,
    method: 'post',
    data
  })
}

export function getIdc(query) {
  return request({
    url: apiuri.idcs,
    method: 'get',
    params: query
  })
}

export function putIdc(id, data) {
  return request({
    url: apiuri.idcs + id + '/',
    method: 'put',
    data
  })
}

export function deleteIdc(id) {
  return request({
    url: apiuri.idcs + id + '/',
    method: 'delete'
  })
}
