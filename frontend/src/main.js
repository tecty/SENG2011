import "@babel/polyfill";
import Vue from "vue";
import "./plugins/vuetify";
import "./plugins/axios";
import "./plugins/vee-validate";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./registerServiceWorker";
import { isLogin } from "./utils/auth";
Vue.config.productionTip = false;
import moment from "moment";

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
// Vue.filters("stateToText", );

Vue.filter("stateToText", s => {
  switch (s) {
    case "BD":
      return "Bidding";
    case "DL":
      return "Deal";
    case "FN":
      return "Finished";
    case "CL":
      return "Canceled";
    case "SD":
      return "Selected";
    case "US":
      return "Unselected";
    default:
      return "Unknown" + s;
  }
});

Vue.filter("showDateTime", s => {
  return moment(s).format("YYYY MMM DD h:mm");
});

new Vue({
  $_veeValidate: {
    validator: "new"
  },
  router,
  store,
  render: h => h(App)
}).$mount("#app");
