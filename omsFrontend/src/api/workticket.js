import request from '@/utils/request'
import { apiuri } from '@/config'

// worktickets
export function postWorkticket(data) {
  return request({
    url: apiuri.worktickers,
    method: 'post',
    data
  })
}

export function getWorkticket(query) {
  return request({
    url: apiuri.worktickers,
    method: 'get',
    params: query
  })
}

export function putWorkticket(id, data) {
  return request({
    url: apiuri.worktickers + id + '/',
    method: 'put',
    data
  })
}

export function patchWorkticket(id, data) {
  return request({
    url: apiuri.worktickers + id + '/',
    method: 'patch',
    data
  })
}

export function deleteWorkticket(id) {
  return request({
    url: apiuri.worktickers + id + '/',
    method: 'delete'
  })
}

// tickettypes
export function postTickettype(data) {
  return request({
    url: apiuri.tickettypes,
    method: 'post',
    data
  })
}

export function getTickettype(query) {
  return request({
    url: apiuri.tickettypes,
    method: 'get',
    params: query
  })
}

export function putTickettype(id, data) {
  return request({
    url: apiuri.tickettypes + id + '/',
    method: 'put',
    data
  })
}

export function deleteTickettype(id) {
  return request({
    url: apiuri.tickettypes + id + '/',
    method: 'delete'
  })
}

// ticketcomments
export function postTicketcomment(data) {
  return request({
    url: apiuri.ticketcomments,
    method: 'post',
    data
  })
}

export function getTicketcomment(query) {
  return request({
    url: apiuri.ticketcomments,
    method: 'get',
    params: query
  })
}

export function putTicketcomment(id, data) {
  return request({
    url: apiuri.ticketcomments + id + '/',
    method: 'put',
    data
  })
}

export function deleteTicketcomment(id) {
  return request({
    url: apiuri.ticketcomments + id + '/',
    method: 'delete'
  })
}

// ticketenclosures
export function postTicketenclosure(data) {
  return request({
    url: apiuri.ticketenclosures,
    method: 'post',
    data
  })
}

export function getTicketenclosure(query) {
  return request({
    url: apiuri.ticketenclosures,
    method: 'get',
    params: query
  })
}

export function deleteTicketenclosure(id) {
  return request({
    url: apiuri.ticketenclosures + id + '/',
    method: 'delete'
  })
}
