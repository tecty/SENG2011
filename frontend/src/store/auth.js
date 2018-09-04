// import all the premitive in the api.js 
import "./api"
import axios from "axios"

const state = {
  token:"",
}

const mutations = {
  ADD_TOKEN(state, token){
    state.token = "JWT "+ token;
  },
  REMOVE_TOKEN(state){
    // remove the token as logged out 
    state.token = "";
  }
}

const actions = {
  loginByCredential({commit}, credential){
    // start loading 
    commit("SET_LOADING");
    
    axios.post("api-token-auth/",credential)
    .then(res => {
      // set the data with success data 
      commit("SUCCESS_AND_SET_DATA",res);
      
      // add token to store 
      commit("ADD_TOKEN",res.data.token);

      // store the token to local storage 
      localStorage.setItem("token", state.token);
    })
    .catch(err => {
      // set up the error message 
      commit("FAIL_AND_SET_DATA",err);
    })
  },
  
}

const getters = {

  // isLogin({state,commit}){
  //   if (state.token == "") {
  //     // here is a token, user must logined 
  //     return true;
  //   }
  //   else{
  //     // try to get the stored item
  //     var token = localStorage.getItem("token");
  //     if(token){
  //       // there is a token in local storage, record it in to vuex
  //       commit("ADD_TOKEN",token);
  //       return true;
  //     }
  //     // else 
  //     return false;
  //   }
  // }
}



export default {
  state,
  actions,
  mutations,
  getters,
}