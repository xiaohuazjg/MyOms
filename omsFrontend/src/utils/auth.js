import Cookies from 'js-cookie'

const TokenKey = 'Token'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

const User = 'XXoo'

export function getUser() {
  return Cookies.get(User)
}

export function setUser(token) {
  return Cookies.set(User, token)
}

export function removeUser() {
  return Cookies.remove(User)
}
