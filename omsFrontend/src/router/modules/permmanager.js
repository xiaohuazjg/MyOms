import Layout from '@/views/layout/Layout'

const Router = {
  name: '权限管理',
  path: '/permmanager',
  component: Layout,
  redirect: 'menus',
  meta: {title: 'permmanager', icon: 'fire'},
  children: [
    {
      path: 'menus',
      component: () => import(('@/views/permmanager/menus')),
      name: '菜单管理',
      meta: {title: 'menus'}
    },
    {
      path: 'menuperm',
      component: () => import(('@/views/permmanager/menuperm')),
      name: '菜单权限',
      meta: {title: 'menuperm'}
    },
    {
      path: 'hostperm',
      component: () => import(('@/views/permmanager/hostperm')),
      name: '主机权限',
      meta: {title: 'hostperm'}
    },
    {
      path: 'wikiperm',
      component: () => import(('@/views/permmanager/wikiperm')),
      name: '文档权限',
      meta: {title: 'wikiperm'}
    }
  ]
}

export default Router
