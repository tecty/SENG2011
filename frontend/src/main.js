import '@babel/polyfill'
import Vue from 'vue'
import './plugins/axios'
import './plugins/vuetify'
import App from './App.vue'
import store from './store'
import router from './router'
// index.js or main.js
import 'vuetify/dist/vuetify.min.css' 
import { isLogin } from './utils/auth';

Vue.config.productionTip = false

// router guard 
router.beforeEach((to, from, next)=>{
  if(to.matched.some(record => record.meta.guest) != true){
    // this record is require authenticate 

    if(isLogin() == false){
      // redirect to the login 
      next({
        path:"/login",
        query:{ redirect: to.fullPath }
      })
      // break this, so it wont goto next 
      return;
    }
  }
  // else go to next route :
  next ();
})


new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
