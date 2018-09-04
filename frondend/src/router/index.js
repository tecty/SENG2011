import Vue from "vue";
import Router from "vue-router";
import AppHome from "@/views/AppHome";
import AppPost from "@/views/AppPost";

Vue.use(Router);

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
});
