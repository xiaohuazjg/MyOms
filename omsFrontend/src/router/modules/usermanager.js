import Layout from '@/views/layout/Layout'

const Router = {
  name: '用户管理',
  path: '/usermanager',
  component: Layout,
  redirect: 'users',
  meta: {title: 'usermanager', icon: 'users'},
  children: [
    {
      path: 'users',
      component: () => import(('@/views/usermanager/users')),
      name: '用户列表',
      meta: {title: 'users'}
    },
    {
      path: 'usergroups',
      component: () => import(('@/views/usermanager/usergroups')),
      name: '用户组列表',
      meta: {title: 'usergroups'}
    },
    {
      path: 'roles',
      component: () => import(('@/views/usermanager/roles')),
      name: '角色列表',
      meta: {title: 'roles'}
    }
  ]
}

export default Router
