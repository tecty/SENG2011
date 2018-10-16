import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
// import api from "./store/api"
// import auth from "./store/auth"
import { LOGIN_FAIL } from "@/store/types";
import { getToken, getUsername } from "./utils/auth";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    api_state: "",
    // base state 
    token: getToken(),
    username: getUsername(),
    error: "",
    data: "",
    posts: []
  },
  mutations: {
    API_ERROR: (state, error_type, error) => {
      // claim an error
      state.api_state = error_type;
      state.error = error;
    },
    ADD_TOKEN: (state, token) => {
      // store this token to local storage
      localStorage.setItem("token", token);
      state.token = token;
    },
    ADD_USER: (state, username) => {
      // store the username in localstorage
      localStorage.setItem("username", username);
      state.username = username;
    },
    REMOVE_TOKEN_AND_USER: state => {
      // remove the record in local storage
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      // remove the vuex record
      state.token = "";
      state.username = "";
      // remove the axios record
      axios.defaults.headers.common["Authorization"] = null;
    },
    GET_POSTS: (state, posts) => {
      state.posts = posts;
    }
  },
  actions: {
    async loginByCredential({ commit, state }, credential) {
      const res = await axios.post("api-token-auth/", credential);
      // add this token to store
      // modify the auth type
      commit("ADD_TOKEN", "JWT " + res.data.token);
      commit("ADD_USER", credential.username);
      // use this token to do axios request
      axios.defaults.headers.common["Authorization"] = state.token;
      // return back this promise back to support chaining
      return res;
    },
    async registerByUser({ dispatch }, user) {
      await axios.post("users/", user);
      dispatch("loginByCredential", {
        username: user.username,
        password: user.password
      });
    },
    logout({ commit }) {
      // remove the record in vuex
      commit("REMOVE_TOKEN_AND_USER");
    },
    placeBid(context, data) {
      return new Promise((resolve, reject) => {
        axios
          .post("bids/", data)
          .then(res => resolve(res))
          .catch(err => reject(err));
      });
    },
    async addPosts({ commit }) {
      const res = await axios.get("posts/");
      // JSON responses are automatically parsed.
      commit("GET_POSTS", res.data);
      return res;
    }
  }
});
