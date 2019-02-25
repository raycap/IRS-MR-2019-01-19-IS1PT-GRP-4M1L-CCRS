import Vue from 'vue'
import Router from 'vue-router'
import QuestionsPage from '../components/pages/QuestionsPage'
import GetStarted from '../components/pages/GetStarted'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'getStartedPage',
      component: GetStarted
    },
    {
      path: '/question',
      name: 'questionsPage',
      component: QuestionsPage
    },
    {path: '*', redirect: { name: 'getStartedPage' }}
  ]
})
