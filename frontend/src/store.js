import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios';
import api from "./store/api"
import auth from "./store/auth"
Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    api,
    auth,
  },
  state: {
  },
  mutations: {

  }
})
