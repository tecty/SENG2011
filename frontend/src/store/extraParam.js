import axios from "axios";

const s = {
  state: {
    extraParameter: {},
    epList: [],
    selected: []
  },
  mutations: {
    SET_EXTRA_PARAMS: (state, ep) => (state.extraParameter = ep),
    PUSH_EMPTY_SELECTED: state => state.selected.push(undefined),
    ADD_SELECTED: (state, data) => {
      state.selected[data.index] = data.id;
    },
    SET_SELECTED: (state, selected) => {
      if (selected) {
        state.selected = selected;
      } else {
        state.selected = [];
      }
    },
    SET_EP_LIST: (state, list) => (state.epList = list)
  },
  actions: {
    async requireExtraParams({ state, commit }) {
      // check wheter the extraparam is loaded
      if (state.epList.length == 0) {
        let ret = await axios.get("Parameters/");
        // store a copy of data to the eplist,
        // which will be use in extraparam vue component
        commit("SET_EP_LIST", ret.data);
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
    },
    getEpById: ({ state }, id) => state.epList.find(el => el.id == id)
  }
};

export default s;
