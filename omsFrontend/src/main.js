import Vue from 'vue'

import Cookies from 'js-cookie'

import 'normalize.css/normalize.css' // A modern alternative to CSS resets

import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import '@/styles/index.scss' // global css

import App from './App'
import store from './store'
import router from './router'

import i18n from './lang' // Internationalization
import './permission' // permission control

import * as filters from './filters' // global filters

/* icon */
import 'vue-awesome/icons/flag'
import 'vue-awesome/icons'
import vIcon from 'vue-awesome/components/Icon'
Vue.component('icon', vIcon)

/* iconfont */
// import Icon from 'vue-icon'
// Vue.use(Icon, 'icon')

/* markdown */
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
Vue.use(mavonEditor)

import 'prismjs/themes/prism-tomorrow.css'

/* calendar */
import fullCalendar from 'vue-fullcalendar'
Vue.component('full-calendar', fullCalendar)

Vue.use(Element, {
  size: Cookies.get('size') || 'medium', // set element-ui default size
  i18n: (key, value) => i18n.t(key, value)
})

// register global utility filters.
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  i18n,
  render: h => h(App)
})
