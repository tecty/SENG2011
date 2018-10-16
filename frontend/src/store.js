import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
// import api from "./store/api"
// import auth from "./store/auth"
import { LOGIN_FAIL } from "@/store/types";
import { getToken } from "./utils/auth";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    api_state: "",
    token: getToken(),
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
      state.token = token;
    },
    REMOVE_TOKEN: state => {
      state.token = "";
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
      // store this token to local storage
      localStorage.setItem("token", state.token);
      // use this token to do axios request
      axios.defaults.headers.common["Authorization"] = state.token;
      // success full do the request
      // return back this promise
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
      // remove the record in local storage
      localStorage.removeItem("token");

      // remove the record in vuex
      commit("REMOVE_TOKEN");
    },
    placeBid(context, data) {
      return new Promise((resolve, reject) => {
        axios
          .post("bids/", data)
          .then(res => resolve(res))
          .catch(err => reject(err));
      });
    },
    addPosts({ commit }) {
      return axios.get("posts/").then(res => {
        // JSON responses are automatically parsed.
        commit("GET_POSTS", res.data);
        return res;
      });
    }
  }
});
