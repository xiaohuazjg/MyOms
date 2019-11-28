import Layout from '@/views/layout/Layout'

const Router = {
  name: '工单系统',
  path: '/worktickets',
  component: Layout,
  redirect: 'worktickets',
  meta: {title: 'workticket', icon: 'leaf'},
  children: [
    {
      path: 'worktickets',
      component: () => import(('@/views/worktickets/worktickets')),
      name: '工单列表',
      meta: {title: 'worktickets'}
    },
    {
      path: 'tickettype',
      component: () => import(('@/views/worktickets/tickettype')),
      name: '工单类型',
      meta: {title: 'tickettype'}
    },
    {
      path: 'addworkticket',
      hidden: true,
      component: () => import(('@/views/worktickets/components/addworkticket')),
      name: '添加工单',
      meta: {title: 'addworkticket'}
    },
    {
      path: 'viewworkticket/:pid',
      hidden: true,
      component: () => import(('@/views/worktickets/components/viewworkticket')),
      name: '查看工单',
      meta: {title: 'viewworkticket'}
    },
    {
      path: 'editworkticket/:pid',
      hidden: true,
      component: () => import(('@/views/worktickets/components/editworkticket')),
      name: '编辑工单',
      meta: {title: 'editworkticket'}
    }
  ]
}

export default Router
