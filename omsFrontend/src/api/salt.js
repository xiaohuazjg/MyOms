import request from '@/utils/request'
import { apiuri } from '@/config'

// salts
export function getCmdrun(data) {
  return request({
    url: apiuri.cmdrun,
    method: 'post',
    data
  })
}

export function getSaltResult(jid) {
  return request({
    url: apiuri.get_cmd_result + jid,
    method: 'get'
  })
}

export function getSyncRemoteServer(method) {
  return request({
    url: apiuri.sync_remote_server + method,
    method: 'get'
  })
}

// saltstates
export function postSaltState(data) {
  return request({
    url: apiuri.saltstates,
    method: 'post',
    data
  })
}

export function getSaltState(query, id) {
  return request({
    url: id ? apiuri.saltstates + id + '/' : apiuri.saltstates,
    method: 'get',
    params: query
  })
}

export function putSaltState(id, data) {
  return request({
    url: apiuri.saltstates + id + '/',
    method: 'put',
    data
  })
}

export function deleteSaltState(id) {
  return request({
    url: apiuri.saltstates + id + '/',
    method: 'delete'
  })
}

// saltstategroups
export function postSaltStateGroup(data) {
  return request({
    url: apiuri.saltstategroups,
    method: 'post',
    data
  })
}

export function getSaltStateGroup(query, id) {
  return request({
    url: id ? apiuri.saltstategroups + id + '/' : apiuri.saltstategroups,
    method: 'get',
    params: query
  })
}

export function putSaltStateGroup(id, data) {
  return request({
    url: apiuri.saltstategroups + id + '/',
    method: 'put',
    data
  })
}

export function deleteSaltStateGroup(id) {
  return request({
    url: apiuri.saltstategroups + id + '/',
    method: 'delete'
  })
}

// saltjobs
export function getSaltStateJob(query) {
  return request({
    url: apiuri.saltjobs,
    method: 'get',
    params: query
  })
}

export function postSaltStateJob(data) {
  return request({
    url: apiuri.saltjobs,
    method: 'post',
    data
  })
}

// update_states_status
export function getUpdateStatesStatus(query) {
  return request({
    url: apiuri.update_states_status,
    method: 'get',
    params: query
  })
}

// get_state_bygroup
export function getStatesStatusBygroup(query) {
  return request({
    url: apiuri.get_state_bygroup,
    method: 'get',
    params: query
  })
}

// saltservers
export function postSaltServer(data) {
  return request({
    url: apiuri.saltservers,
    method: 'post',
    data
  })
}

export function getSaltServer(query, id) {
  return request({
    url: id ? apiuri.saltservers + id + '/' : apiuri.saltservers,
    method: 'get',
    params: query
  })
}

export function putSaltServer(id, data) {
  return request({
    url: apiuri.saltservers + id + '/',
    method: 'put',
    data
  })
}

export function deleteSaltServer(id) {
  return request({
    url: apiuri.saltservers + id + '/',
    method: 'delete'
  })
}
