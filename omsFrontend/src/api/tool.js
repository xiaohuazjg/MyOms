import request from '@/utils/request'
import { apiuri } from '@/config'

// upload
export function postUpload(data) {
  return request({
    url: apiuri.uploads,
    method: 'post',
    data
  })
}

export function getUpload(query, id) {
  return request({
    url: id ? apiuri.uploads + id + '/' : apiuri.uploads,
    method: 'get',
    params: query
  })
}

export function deleteUpload(id) {
  return request({
    url: apiuri.uploads + id + '/',
    method: 'delete'
  })
}

// sendmail
export function postSendmail(data) {
  return request({
    url: apiuri.sendmail,
    method: 'post',
    data
  })
}

// sendmessage
export function postSendmessage(data) {
  return request({
    url: apiuri.sendmessage,
    method: 'post',
    data
  })
}

// calenders
export function postCalender(data) {
  return request({
    url: apiuri.calenders,
    method: 'post',
    data
  })
}

export function getCalender(query, id) {
  return request({
    url: id ? apiuri.calenders + id + '/' : apiuri.calenders,
    method: 'get',
    params: query
  })
}

export function deleteCalender(id) {
  return request({
    url: apiuri.calenders + id + '/',
    method: 'delete'
  })
}

// records
export function postRecord(data) {
  return request({
    url: apiuri.records,
    method: 'post',
    data
  })
}

export function getRecord(query, id) {
  return request({
    url: apiuri.records,
    method: 'get',
    params: query
  })
}
