import Layout from '@/views/layout/Layout'

const Router = {
  name: 'salt管理',
  path: '/saltmanager',
  component: Layout,
  redirect: 'cmdrun',
  meta: {title: 'saltmanager', icon: 'cube'},
  children: [
    {
      path: 'cmdrun',
      component: () => import(('@/views/saltmanager/cmdrun')),
      name: '执行命令',
      meta: {title: 'cmdrun'}
    },
    {
      path: 'state',
      component: () => import(('@/views/saltmanager/state')),
      name: 'state管理',
      meta: {title: 'state'}
    },
    {
      path: 'runstate',
      component: () => import(('@/views/saltmanager/runstate')),
      name: '执行state',
      meta: {title: 'runstate'}
    }
  ]
}

export default Router
