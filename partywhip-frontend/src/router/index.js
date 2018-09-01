import Vue from 'vue'
import Router from 'vue-router'
import AppHome from '@/components/AppHome'
import AppPost from '@/components/AppPost'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AppHome',
      component: AppHome
    },
    {
      path: '/post',
      name: 'AppPost',
      component: AppPost
    }
  ]
})
