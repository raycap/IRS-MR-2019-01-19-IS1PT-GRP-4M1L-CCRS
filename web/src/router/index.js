import Vue from 'vue'
import Router from 'vue-router'
import QuestionsPage from '../components/QuestionsPage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'questionsPage',
      component: QuestionsPage
    },
    {
      path: '/question',
      name: 'questionsPage',
      component: QuestionsPage
    },
    {path: '*', redirect: { name: 'questionsPage' }}
  ]
})
