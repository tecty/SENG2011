import Vue from "vue";
import Router from "vue-router";
import AppHome from "@/views/AppHome.vue";
import { isLogin } from "@/utils/auth";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: AppHome,
      meta: {
        // key to let the view can be view from guest
        guest: true
      }
    },
    {
      path: "/about",
      name: "about",
      component: () => import("@/views/About.vue"),
      meta: {
        // key to let the view can be view from guest
        guest: true
      }
    },
    {
      path: "/post",
      name: "post",
      component: () => import("@/views/AppPost.vue")
    },
    {
      path: "/login",
      name: "login",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */
        "@/views/Login.vue"),
      meta: {
        // key to let the view can be view from guest
        guest: true
      },
      beforeEnter: (to, from, next) => {
        // if user is currently logged in, prevent him from hitting this page.
        if (isLogin()) {
          next("/");
        }
      }
    }
  ]
});
