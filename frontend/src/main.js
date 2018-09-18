import "@babel/polyfill";
import Vue from "vue";
import "./plugins/vuetify";
import "./plugins/axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./registerServiceWorker";
import { isLogin } from "./utils/auth";

Vue.config.productionTip = false;

// router guard
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.guest) != true) {
    // this record is require authenticate

    if (!isLogin()) {
      // redirect to the login
      next({
        name: "login",
        query: { redirect: to.fullPath }
      });
      // break this, so it wont goto next
      return;
    }
  }
  // else go to next route :
  next();
});

new Vue({
  router,
  store,
  render: h => h(App),
  created() {
    this.$store.dispatch('addPosts')
  }
}).$mount("#app");
