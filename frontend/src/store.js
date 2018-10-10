import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
// import api from "./store/api"
// import auth from "./store/auth"
import { LOGIN_FAIL } from "@/store/types";
import { getToken } from "./utils/auth";

Vue.use(Vuex);

export default new Vuex.Store({
  // modules:{
  //   api,
  //   auth,
  // },
  state: {
    api_state: "",
    token: getToken(),
    error: "",
    data: "",
    posts: []
  },
  getters: {
    currPost: state => {
      return state.posts.find(post => post.id == this.$route.params.postId - 1);
    }
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
    SET_POSTS: (state, posts) => {
      state.posts = posts;
    }
  },
  actions: {
    loginByCredential({ commit, state }, credential) {
      return new Promise((resolve, reject) => {
        axios
          .post("api-token-auth/", credential)
          .then(res => {
            // add this token to store
            // modify the auth type
            commit("ADD_TOKEN", "JWT " + res.data.token);
            // store this token to local storage
            localStorage.setItem("token", state.token);
            localStorage.setItem("username", credential.username);
            // use this token to do axios request
            axios.defaults.headers.common["Authorization"] = state.token;

            // success full do the request

            resolve();
          })
          .catch(err => {
            commit("API_ERROR", LOGIN_FAIL, err);
            // reject by the server
            reject(err);
          });
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
          .then(res => {
            console.log("bid success");
            resolve(res);
          })
          .catch(err => reject(err));
      });
    },
    addPosts({ commit }) {
      return new Promise((resolve, reject) => {
        axios
          .get("posts/")
          .then(response => {
            // JSON responses are automatically parsed.
            console.log(response);
            console.log(response.data);
            commit("SET_POSTS", response.data);
            resolve(this.state.posts);
          })
          .catch(error => {
            console.log(error);
            console.log(error.response);
            reject();
          });
      });
    }
    // updatePost(context, id, data) {
    //   return new Promise((resolve, reject) => {
    //     axios
    //       .put("posts/" + id, data)
    //       .then(response => {
    //         // JSON responses are automatically parsed.
    //         console.log(response);
    //         console.log(response.data);
    //         resolve();
    //       })
    //       .catch(error => {
    //         console.log(error);
    //         console.log(error.response);
    //         reject();
    //       });
    //   });
    // }
  }
});
