import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/views/layout/Layout'

/** note: sub-menu only appear when children.length>=1
 *  detail see  https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 **/

/**
 * hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
 *                                if not set alwaysShow, only more than one route under the children
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noredirect           if `redirect:noredirect` will no redirect in the breadcrumb
 * title:'router-title'             the title is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    will control the page roles (you can set multiple roles)
    title: 'title'               the title show in sub-menu and breadcrumb (recommend set)
    icon: 'svg-title'             the icon show in the sidebar
    noCache: true                if true, the page will no be cached(default is false)
    breadcrumb: false            if false, the item will hidden in breadcrumb(default is true)
    affix: true                  if true, the tag will affix in the tags-view
  }
 **/
export const baseRouterMap = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path*',
        component: () => import('@/views/redirect/index')
      }
    ]
  },
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/auth-redirect',
    component: () => import('@/views/login/authredirect'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/errorPage/404'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/errorPage/401'),
    hidden: true
  },
  {
    path: '',
    component: Layout,
    redirect: 'dashboard',
    children: [
      {
        path: 'dashboard',
        component: () => import('@/views/dashboard/index'),
        name: '首页',
        meta: {title: 'dashboard', icon: 'home', noCache: true, affix: true}
      }
    ]
  }
]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({y: 0}),
  routes: baseRouterMap
})

/* Router Modules */
import usermanagerRouter from './modules/usermanager'
import wikimanagerRouter from './modules/wikimanager'
import permmanagerRouter from './modules/permmanager'
import workticketRouter from './modules/workticket'
import deploymanagerRouter from './modules/deploymanager'
import saltmanagerRouter from './modules/saltmanager'
import hostmanagerRouter from './modules/hostmanager'

export const asyncRouterMap = [
  usermanagerRouter,
  wikimanagerRouter,
  permmanagerRouter,
  workticketRouter,
  deploymanagerRouter,
  saltmanagerRouter,
  hostmanagerRouter,
  {
    name: '工具管理',
    path: '/toolmanager',
    component: Layout,
    redirect: 'upload',
    meta: {title: 'toolmanager', icon: 'cogs'},
    children: [
      {
        path: 'upload',
        component: () => import(('@/views/toolmanager/upload')),
        name: '上传列表',
        meta: {title: 'upload'}
      }
    ]
  }
]

export const errorRouterMap = [
  {path: '*', redirect: '/404', hidden: true}
]
