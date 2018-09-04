import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';
// import api from "./store/api"
// import auth from "./store/auth"
import {LOGIN_FAIL} from  "@/store/types";

Vue.use(Vuex)



export default new Vuex.Store({
  // modules:{
  //   api,
  //   auth,
  // },
  state: {
    api_state:"",
    token:"",
    error: "",
    data: "",
  },
  mutations: {
    API_ERROR:(state, error_type, error)=>{
      // claim an error 
      state.api_state = error_type;
      state.error = error;
    },
    ADD_TOKEN:(state,token)=>{
      state.token = "JWT "+ token;
    },
    REMOVE_TOKEN: (state)=>{
      state.token = "";
    }

  },
  actions:{
    loginByCredential({commit,state},credential){
      return new Promise((resolve, reject)=>{
        axios.post("api-token-auth/",credential)
        .then(res =>{
          // add this token to store
          commit("ADD_TOKEN",res.data.token);
          // store this token to local storage 
          localStorage.setItem("token",state.token);
          // use this token to do axios request  
          axios.defaults.headers.common['Authorization'] = state.token;
          
          // success full do the request 
          resolve();
        })
        .catch(err =>{
          commit("API_ERROR",LOGIN_FAIL,err);
          // reject by the server 
          reject(err);
        })
      })
    },
    logout({commit}){
      // remove the record in local storage 
      localStorage.removeItem("token");

      // remove the record in vuex 
      commit("REMOVE_TOKEN");
    },
    isLogin({state,commit}){
      if(state.token ){
        return true; 
      }
      else {
        // try to fetch from the local storage 
        var token = localStorage.getItem("token");
        if (token){
          // add this token to store
          commit("ADD_TOKEN",token);
          // store this token to local storage 
          localStorage.setItem("token",state.token);
          // use this token to do axios request  
          axios.defaults.headers.common['Authorization'] = state.token;
          return true;
        }
      }
      // else: couldn't find token anywhere
      return false;
    }
  }

})
