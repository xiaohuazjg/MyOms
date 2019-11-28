import Layout from '@/views/layout/Layout'

const Router = {
  name: '文档管理',
  path: '/wikimanager',
  component: Layout,
  redirect: 'noredirect',
  meta: {title: 'wikimanager', icon: 'paper-plane'},
  children: [
    {
      path: 'wikiadmin',
      component: () => import(('@/views/wikimanager/wikiadmin')),
      name: '文档后台',
      meta: {title: 'wikiadmin'}
    },
    {
      path: 'wikicenter',
      component: () => import(('@/views/wikimanager/wikicenter')),
      name: '文档中心',
      meta: {title: 'wikicenter'}
    },
    {
      path: 'addwiki',
      hidden: true,
      component: () => import(('@/views/wikimanager/components/addwiki')),
      name: '添加文档',
      meta: {title: 'addwiki'}
    },
    {
      path: 'editwiki/:wikiid',
      hidden: true,
      component: () => import(('@/views/wikimanager/components/editwiki')),
      name: '编辑文档',
      meta: {title: 'editwiki'}
    },
    {
      path: 'viewwiki/:wikiid',
      hidden: true,
      component: () => import(('@/views/wikimanager/components/viewwiki')),
      name: '查看文档',
      meta: {title: 'viewwiki'}
    }
  ]
}

export default Router
