'use strict'
// Template version: 1.2.6
// see http://vuejs-templates.github.io/webpack for documentation.

const path = require('path')

module.exports = {
  title: '运维管理系统',
  super_group: 'admin',

  // pagination
  LIMIT: 10,
  pagesize: [10, 20, 50, 100],
  pageformat: 'total, prev, pager, next, sizes',

  // cdenv
  dev: {
    // Paths
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    proxyTable: {},

    // Various Dev Server settings

    // can be overwritten by process.env.HOST
    // if you want dev by ip, please set host: '0.0.0.0'
    host: 'localhost',
    port: 8080, // can be overwritten by process.env.PORT, if port is in use, a free one will be determined
    autoOpenBrowser: true,
    errorOverlay: true,
    notifyOnErrors: false,
    poll: false, // https://webpack.js.org/configuration/dev-server/#devserver-watchoptions-

    // Use Eslint Loader?
    // If true, your code will be linted during bundling and
    // linting errors and warnings will be shown in the console.
    useEslint: false,
    // If true, eslint errors and warnings will also be shown in the error overlay
    // in the browser.
    showEslintErrorsInOverlay: false,

    /**
     * Source Maps
     */

    // https://webpack.js.org/configuration/devtool/#development
    devtool: 'cheap-source-map',

    // CSS Sourcemaps off by default because relative paths are "buggy"
    // with this option, according to the CSS-Loader README
    // (https://github.com/webpack/css-loader#sourcemaps)
    // In our experience, they generally work as expected,
    // just be aware of this issue when enabling this option.
    cssSourceMap: false
  },

  build: {
    // Template for index.html
    index: path.resolve(__dirname, '../dist/index.html'),

    // Paths
    assetsRoot: path.resolve(__dirname, '../dist'),
    assetsSubDirectory: 'static',

    /**
     * You can set by youself according to actual condition
     * You will need to set this if you plan to deploy your site under a sub path,
     * for example GitHub pages. If you plan to deploy your site to https://foo.github.io/bar/,
     * then assetsPublicPath should be set to "/bar/".
     * In most cases please use '/' !!!
     */
    assetsPublicPath: '/',

    /**
     * Source Maps
     */
    productionSourceMap: false,
    // https://webpack.js.org/configuration/devtool/#production
    devtool: 'source-map',

    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to 'true', make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ['js', 'css'],

    // Run the build command with an extra argument to
    // View the bundle analyzer report after build finishes:
    // 'npm run build:prod --report'
    // Set to 'true' or 'false' to always turn it on or off
    bundleAnalyzerReport: process.env.npm_config_report || false,

    // 'npm run build:prod --generate_report'
    generateAnalyzerReport: process.env.npm_config_generate_report || false
  },
  apiuri: {
    // 登录
    login: '/api/api-token-auth/',
    logout: '/api/api-auth/logout/',
    changePassword: '/api/changepasswd/',

    // 用户
    users: '/api/users/',
    groups: '/api/groups/',
    roles: '/api/roles/',

    // 工单
    worktickers: '/api/worktickers/',
    ticketcomments: '/api/ticketcomments/',
    ticketenclosures: '/api/ticketenclosures/',
    tickettypes: '/api/tickettypes/',

    // 权限
    usermenuperms: '/api/usermenuperms/',
    userhostperms: '/api/userhostperms/',
    userwikiperms: '/api/userwikiperms/',
    routerinfo: '/api/routers/',

    // 菜单
    firstmenus: '/api/firstmenus/',
    secondmenus: '/api/secondmenus/',
    menumetas: '/api/menumetas/',

    // tools
    uploads: '/api/upload/',
    sendmail: '/api/sendmail/',
    sendmessage: '/api/sendmessage/',
    calenders: '/api/calenders/',

    // 文档平台
    wikis: '/api/wikis/',
    opswikis: '/api/opswikis/',

    // 发布
    jobs: '/api/jobs/',
    deployenvs: '/api/deployenvs/',
    deployjobs: '/api/deployjobs/',
    deployresults: '/api/deployresults/',
    updaejobsstatus: '/api/update_jobs_status/',
    deploycmds: '/api/deploycmds/',
    deployversions: '/api/deployversions/',

    // 发布工单
    deploytickets: '/api/deploytickets/',
    deployticketenclosures: '/api/deployticketenclosures/',
    sqltickets: '/api/sqltickets/',

    // salt
    saltservers: '/api/saltservers/',
    saltstates: '/api/saltstates/',
    saltstategroups: '/api/saltstategroups/',
    saltjobs: '/api/saltjobs/',
    cmdrun: '/api/salts/cmdrun/',
    get_cmd_result: '/api/salts/get_cmd_result/',
    update_states_status: '/api/update_states_status/',
    get_state_bygroup: '/api/get_state_bygroup/',
    sync_remote_server: '/api/salts/sync_remote_server/',

    // 主机
    hosts: '/api/hosts/',
    idcs: '/api/idcs/',
    records: '/api/records/',
  }
}
