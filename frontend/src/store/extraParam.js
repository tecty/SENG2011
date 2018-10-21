import axios from "axios";

const s = {
  state: {
    extraParameter: {},
    selected: []
  },
  mutations: {
    SET_EXTRA_PARAMS: (state, ep) => (state.extraParameter = ep),
    CLEAR_SELECTED: state => {
      state.selected = [];
    },
    ADD_SELECTED: (state, data) => {
      state.selected[data.index] = data.id;
    }
  },
  actions: {
    async requireExtraParams({ state, commit }) {
      // check wheter the extraparam is loaded
      if (Object.keys(state.extraParameter).length === 0) {
        let ret = await axios.get("Parameters/");
        let obj = {};
        // construct the tree like object
        ret.data.forEach(el => {
          if (!(el.key in obj)) {
            obj[el.key] = [];
          }
          // push a new object which will have the id and value paire.
          obj[el.key].push({
            value: el.id,
            text: el.value
          });
        });
        // push the treelike object into the vuex
        commit("SET_EXTRA_PARAMS", obj);
        return ret;
      }
    }
  }
};

export default s;
