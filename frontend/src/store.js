import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import { getToken, getUsername } from "./utils/auth";
import moment from "moment";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    api_state: "",
    // base state
    token: getToken(),
    username: getUsername(),
    error: "",
    data: "",
    posts: [],
    events: [],
    extraParameter: []
  },
  mutations: {
    API_ERROR: (state, error_type, error) => {
      // claim an error
      state.api_state = error_type;
      state.error = error;
    },
    API_WAITING: state => {
      state.api_state = "WAIT";
    },
    API_FINISHED: state => {
      state.api_state = "";
    },
    API_READY: state => {
      state.api_state = "READY";
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
    SET_POSTS: (state, posts) => {
      state.posts = posts;
    },
    SET_EVENTS: (state, events) => {
      state.events = events;
    },
    SET_EXTRA_PARAMS: (state, ep) => (state.extraParameter = ep)
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
    async refreshPosts({ commit }) {
      const res = await axios.get("posts/");
      // JSON responses are automatically parsed.
      commit("SET_POSTS", res.data);
      return res;
    },
    async refreshEvents({ commit }) {
      const res = await axios.get("events/");
      res.data.forEach(e => {
        e.eventTime = moment(e.eventTime).format("YYYY MMM DD h:mm");
        e.bidClosingTime = moment(e.bidClosingTime).format("YYYY MMM DD h:mm");
      });
      commit("SET_EVENTS", res.data);
      return res;
    },
    async refreshAll({ dispatch, commit }) {
      commit("API_WAITING");
      return Promise.all([
        dispatch("refreshEvents"),
        dispatch("refreshPosts")
      ]).then(res => {
        dispatch("wireEvents").then(() => commit("API_FINISHED"));
        return res;
      });
    },
    async wireEvents({ state, commit }) {
      let posts = state.posts;
      posts.forEach(p => {
        // wire all the posts with it's event
        p.event = state.events.find(e => e.id == p.event);
      });
      // commit these wired post into store
      commit("SET_POSTS", posts);
    },
    async getPostById({ state }, id) {
      return state.posts.find(el => el.id == id);
    },
    async getEventById({ state }, id) {
      return state.events.find(el => el.id == id);
    },
    async requireExtraParams({ state, commit }) {
      if (state.extraParameter.length == 0) {
        let ret = await axios.get("Parameters/");
        commit("SET_EXTRA_PARAMS", ret.data);
        return ret;
      }
      return null;
    },
    async createPost({ commit }, data) {
      commit("API_WAITING");
      let ret = await axios.post("posts/", data);
      commit("API_FINISHED");
      return ret;
    },
    async createEvent({ commit }, data) {
      commit("API_WAITING");
      let ret = await axios.post("events/", data);
      commit("API_FINISHED");
      return ret;
    },
    async createMsg(store, data) {
      let ret = await axios.post("msgs/", data);
      return ret;
    },
    async chooseBidById({ commit }, postId, bidId) {
      commit("API_WAITING");
      let ret = await axios.post(`posts/${postId}/choose/`, { id: bidId });
      commit("API_FINISHED");
      return ret;
    },
    async deleteBidById({ commit }, bidId) {
      commit("API_WAITING");
      // send the actual delete
      let ret = await axios.delete(`bids/${bidId}/`);
      commit("API_FINISHED");
      return ret;
    }
  }
});
