import Layout from '@/views/layout/Layout'

const Router = {
  name: '发布系统',
  path: '/deploymanager',
  component: Layout,
  redirect: 'deployjobs',
  meta: {title: 'deploymanager', icon: 'tasks'},
  children: [
    {
      path: 'deployjobs',
      component: () => import(('@/views/deploymanager/deployjobs')),
      name: '项目列表',
      meta: {title: 'deployjobs'}
    },
    {
      path: 'jobtickets',
      component: () => import(('@/views/deploymanager/jobtickets')),
      name: '发布申请',
      meta: {title: 'jobtickets'}
    },
    {
      path: 'runjob/:job_id',
      hidden: true,
      component: () => import(('@/views/deploymanager/components/runjob')),
      name: '构建项目',
      meta: {title: 'runjob'}
    },
    {
      path: 'sqltickets',
      component: () => import(('@/views/deploymanager/sqltickets')),
      name: 'SQL执行申请',
      meta: {title: 'sqltickets'}
    }
  ]
}

export default Router
