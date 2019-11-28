import request from '@/utils/request'
import { apiuri } from '@/config'

// usermenuperms
export function postMenuPerm(data) {
  return request({
    url: apiuri.usermenuperms,
    method: 'post',
    data
  })
}

export function getMenuPerm(query, id) {
  return request({
    url: apiuri.usermenuperms,
    method: 'get',
    params: query
  })
}

export function putMenuPerm(id, data) {
  return request({
    url: apiuri.usermenuperms + id + '/',
    method: 'put',
    data
  })
}

export function deleteMenuPerm(id) {
  return request({
    url: apiuri.usermenuperms + id + '/',
    method: 'delete'
  })
}

// userhostperms
export function postHostPerm(data) {
  return request({
    url: apiuri.userhostperms,
    method: 'post',
    data
  })
}

export function getHostPerm(query, id) {
  return request({
    url: apiuri.userhostperms,
    method: 'get',
    params: query
  })
}

export function putHostPerm(id, data) {
  return request({
    url: apiuri.userhostperms + id + '/',
    method: 'put',
    data
  })
}

export function deleteHostPerm(id) {
  return request({
    url: apiuri.userhostperms + id + '/',
    method: 'delete'
  })
}

// userwikiperms
export function postWikiPerm(data) {
  return request({
    url: apiuri.userwikiperms,
    method: 'post',
    data
  })
}

export function getWikiPerm(query, id) {
  return request({
    url: apiuri.userwikiperms,
    method: 'get',
    params: query
  })
}

export function putWikiPerm(id, data) {
  return request({
    url: apiuri.userwikiperms + id + '/',
    method: 'put',
    data
  })
}

export function deleteWikiPerm(id) {
  return request({
    url: apiuri.userwikiperms + id + '/',
    method: 'delete'
  })
}
