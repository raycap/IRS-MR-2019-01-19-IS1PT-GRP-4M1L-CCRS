// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/store'
import {pageName} from './commons/constants/constants'

Vue.config.productionTip = false

router.afterEach((to, from) => {
  if (from.name === pageName.recommendPage && to.name === pageName.getStarted) {
    window.location.reload(true)
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
