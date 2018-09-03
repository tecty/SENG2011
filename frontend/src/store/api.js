import {API_SUCCESS , API_FAIL } from './types'

const state = {
  state: API_SUCCESS,
  loading: false,
  error: "",
  data:"",
}

const mutations = {
  SET_LOADING(state){
    // change the loging state to true 
    state.loading = true;
  },
  SUCCESS_AND_SET_DATA(state,data){
    // cacel the loading state
    state.loading = false;
    // refresh the api state 
    state.state = API_SUCCESS;

    // commit the data 
    state.data = data;
    
  },
  FAIL_AND_SET_DATA(state,data){
    // cacel the loading state
    state.loading = false;
    // refresh the api state 
    state.state = API_FAIL;
    // commit the data 
    state.data = data;
  },
}

const actions = {
  
}

const getters = {
  isApiSuccess(state){
    return (state.state == API_SUCCESS);
  }
}


export default {
  state,
  actions,
  mutations,
  getters
}