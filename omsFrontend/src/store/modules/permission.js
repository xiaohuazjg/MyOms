import { asyncRouterMap, baseRouterMap, errorRouterMap } from '@/router'

/**
 * 通过meta.role判断是否与当前用户权限匹配
 * @param roles
 * @param route
 */
function hasPermission(menus, route) {
  if (route.name) {
    if (menus[route.name] !== undefined) {
      return menus[route.name]
    } else {
      return false
    }
  } else {
    return true
  }
}

/**
 * 递归过滤异步路由表，返回符合用户角色权限的路由表
 * @param menus asyncRouterMap
 * @param menus
 */
function filterAsyncRouter(asyncRouterMap, menus) {
  const accessedRouters = asyncRouterMap.filter(route => {
    if (hasPermission(menus, route)) {
      if (route.children && route.children.length) {
        route.children = filterAsyncRouter(route.children, menus)
      }
      return true
    }
    return false
  })
  return accessedRouters
}


const permission = {
  state: {
    routers: [],
    addRouters: []
  },
  mutations: {
    setRouters: (state, routers) => {
      state.addRouters = routers
      state.routers = baseRouterMap.concat(routers)
    }
  },
  actions: {
    GenerateRoutes({ commit }, { role, menus }) {
      return new Promise(resolve => {
        let accessedRouters
        if (role === 'admin') {
          commit('setRouters', accessedRouters)
          accessedRouters = asyncRouterMap.concat(errorRouterMap)
        } else {
          accessedRouters = filterAsyncRouter(asyncRouterMap, menus).concat(errorRouterMap)
        }
        commit('setRouters', accessedRouters)
        resolve()
      })
    }
  }
}

export default permission
