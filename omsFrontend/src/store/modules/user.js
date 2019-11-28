import {loginByUsername, getUserInfo, getRouterInfo} from '@/api/login'
import {getToken, setToken, removeToken, setUser, getUser} from '@/utils/auth'
import {super_group} from '@/config'

const user = {
  state: {
    username: getUser(),
    token: getToken(),
    avatar: '',
    groups: [],
    role: '',
    hasGetInfo: false,
    menus: undefined,
    elements: undefined,
    permMenus: undefined
  },

  mutations: {
    setToken: (state, token) => {
      state.token = token
      setToken(token)
    },
    setUsername: (state, username) => {
      state.username = username
      setUser(username)
    },
    setAvatar: (state, avatar) => {
      state.avatar = avatar
    },
    setGroups: (state, groups) => {
      state.groups = groups
    },
    setRole: (state, role) => {
      state.role = role
    },
    setHasGetInfo: (state, status) => {
      state.hasGetInfo = status
    },
    setMenus: (state, menus) => {
      state.menus = menus
    },
    setElements: (state, elements) => {
      state.elements = elements
    },
    setPermMenus: (state, permMenus) => {
      state.roles = permMenus
    }
  },

  actions: {
    // 用户名登录
    LoginByUsername({commit}, userInfo) {
      userInfo.username = userInfo.username.trim()
      return new Promise((resolve, reject) => {
        loginByUsername(userInfo).then(response => {
          commit('setToken', response.data.token)
          commit('setUsername', userInfo.username)
          commit('setHasGetInfo', true)
          commit('setMenus', undefined)
          commit('setElements', undefined)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },

    // 获取用户信息
    GetUserInfo({commit, state}) {
      return new Promise((resolve, reject) => {
        const data = {
          username: state.username
        }
        getUserInfo(data).then(response => {
          const data = response.data[0]
          commit('setAvatar', data.avatar)
          commit('setGroups', data.groups)
          // commit('setRole', data.role)
          resolve(response)
        }).catch(error => {
          console.log(error)
          reject(error)
        })
      })
    },

    // 获取用户路由权限
    GetUserRouterInfo({commit, state}) {
      return new Promise((resolve, reject) => {
        const data = {
          username: state.username
        }
        getRouterInfo(data).then(response => {
          const data = response.data
          const groups = data.groups
          commit('setGroups', groups)
          localStorage.setItem('groups', groups)
          console.log('super_group: ' + super_group)
          if (groups.indexOf(super_group) >= 0) {
            commit('setRole', 'admin')
          } else {
            commit('setRole', 'test')
          }
          const menus = {}
          for (const i of data.menus) {
            menus[i] = true
          }
          commit('setMenus', menus)
          const elements = {}
          for (const i of data.elements) {
            elements[i] = true
          }
          commit('setElements', elements)
          resolve(response)
        }).catch(error => {
          console.log(error)
          reject(error)
        })
      })
    },

    // 登出
    LogOut({commit, state}) {
      return new Promise((resolve, reject) => {
        commit('setToken', '')
        commit('setAvator', '')
        commit('setGroups', [])
        commit('setRole', '')
        removeToken()
        commit('setMenus', undefined)
        commit('setElements', undefined)
        commit('setPermMenus', undefined)
        resolve()
      })
    },

    // 动态修改权限
    ChangeRoles({commit, dispatch}, role) {
      return new Promise(resolve => {
        commit('setToken', role)
        setToken(role)
        getUserInfo(role).then(response => {
          const data = response.data
          commit('setRoles', data.roles)
          commit('setUsername', data.name)
          commit('setAvator', data.avatar)
          dispatch('GenerateRoutes', data) // 动态修改权限后 重绘侧边菜单
          resolve()
        })
      })
    }
  }
}

export default user
