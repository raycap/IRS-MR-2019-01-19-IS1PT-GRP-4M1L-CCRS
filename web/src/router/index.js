import Vue from 'vue'
import Router from 'vue-router'
import QuestionsPage from '../components/pages/QuestionsPage'
import GetStarted from '../components/pages/GetStarted'
import RecommendPage from '../components/pages/RecommendPage'
import {pageName} from '../commons/constants/constants'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/home',
      name: pageName.getStarted,
      component: GetStarted
    },
    {
      path: '/question/:page/',
      name: pageName.questionsPage,
      component: QuestionsPage
    },
    {
      path: '/result',
      name: pageName.recommendPage,
      component: RecommendPage
    },
    {path: '*', redirect: { name: pageName.getStarted }}
  ]
})
