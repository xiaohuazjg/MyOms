import Layout from '@/views/layout/Layout'

const Router = {
  name: '主机管理',
  path: '/hostmanager',
  component: Layout,
  redirect: 'hosts',
  meta: {title: 'hostmanager', icon: 'desktop'},
  children: [
    {
      path: 'hosts',
      component: () => import(('@/views/hostmanager/hosts')),
      name: '主机列表',
      meta: {title: 'hosts'}
    },
    {
      path: 'idcs',
      component: () => import(('@/views/hostmanager/idcs')),
      name: '机房列表',
      meta: {title: 'idcs'}
    },
    {
      path: 'assetrecords',
      component: () => import(('@/views/hostmanager/assetrecords')),
      name: '主机修改记录',
      meta: {title: 'assetrecords'}
    }
  ]
}

export default Router
