import Vue from 'vue'
import Vuex from 'vuex'
import './plugins/axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token:""
  },
  mutations: {
    TOKEN_ADD:(state,token)=>{
      // add this token to store
      state.token = token;
      // store this token to the local storage 
      localStorage.setItem('token',token);
    }
  },
  actions: {
    loginByCredential({commit}, credential){
      axios.post('api-token-auth/', credential)
      .then(res => {
        // push the token name with JWT 
        let token ="JWT "+res.data.token; 
        // checkout to login state
        axios.defaults.headers.common['Authorization'] = token;
        // commit this token to vuex
        // to store it.
        commit('TOKEN_ADD',token);
      })
    }
  }
})
