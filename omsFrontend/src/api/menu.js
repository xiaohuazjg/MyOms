import request from '@/utils/request'
import { apiuri } from '@/config'

// firstmenus
export function postFirstmenus(data) {
  return request({
    url: apiuri.firstmenus,
    method: 'post',
    data
  })
}

export function getFirstmenus(query, id) {
  return request({
    url: id ? apiuri.firstmenus + id + '/' : apiuri.firstmenus,
    method: 'get',
    params: query
  })
}

export function putFirstmenus(id, data) {
  return request({
    url: apiuri.firstmenus + id + '/',
    method: 'put',
    data
  })
}

export function deleteFirstmenus(id) {
  return request({
    url: apiuri.firstmenus + id + '/',
    method: 'delete'
  })
}

// secondmenus
export function postSecondmenus(data) {
  return request({
    url: apiuri.secondmenus,
    method: 'post',
    data
  })
}

export function getSecondmenus(query, id) {
  return request({
    url: id ? apiuri.secondmenus + id + '/' : apiuri.secondmenus,
    method: 'get',
    params: query
  })
}

export function putSecondmenus(id, data) {
  return request({
    url: apiuri.secondmenus + id + '/',
    method: 'put',
    data
  })
}

export function deleteSecondmenus(id) {
  return request({
    url: apiuri.secondmenus + id + '/',
    method: 'delete'
  })
}

// menumetas
export function postMenumetas(data) {
  console.log(data)
  return request({
    url: apiuri.menumetas,
    method: 'post',
    data
  })
}

export function getMenumetas(query, id) {
  return request({
    url: id ? apiuri.menumetas + id + '/' : apiuri.menumetas,
    method: 'get',
    params: query
  })
}

export function putMenumetas(id, data) {
  return request({
    url: apiuri.menumetas + id + '/',
    method: 'put',
    data
  })
}

export function deleteMenumetas(id) {
  return request({
    url: apiuri.menumetas + id + '/',
    method: 'delete'
  })
}
