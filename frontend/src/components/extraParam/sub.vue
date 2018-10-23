<template>
  <v-layout row fill-height>
    <v-flex xs12 sm6>
      <!-- selection of the key  -->
      {{ key }}
      <v-select
        v-model="key"
        :items="keyList"
        label="Extra Requirement"
      />
    </v-flex >
    <v-flex xs12 sm6>
      {{id }}
      <!-- selection of the value -->
      <v-select v-if="key" :items="valList" v-model="value" />
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  props: ["index", "value"],
  data() {
    return {
      // record the temporary selection of key by user 
      tmpKey: "",
      id: ""
    };
  },
  computed: {
    ...mapState({
      eps: state => state.extraParam.extraParameter,
      keyList: state => {
        return Object.keys(state.extraParam.extraParameter);
      }
    }),
    valList() {
      if (this.key) {
        return this.eps[this.key];
      }
      return [];
    },
    key: {
      get: () =>{
        if (value) {
          // there's a selected ep
          let selectedEp = this.eps.find( ep => ep.id == value);
          // setup the tmp key 
          this.tmpKey = selectedEp.key;
        }
        return this.tmpKey;
      },
      set: (newKey) => {
        if (newKey != this.tmpKey){
          // try to update and revoke the value 
          this.value = undefined;
          // set the tmp key to new one 
          this.tmpKey = newKey;
        }
      }
    }
  },
  methods: {
    ...mapMutations(["ADD_SELECTED"]),
    declearChange() {
      // add this selected id
      this.ADD_SELECTED({
        index: this.index,
        id: this.id
      });
      // emit a changed event
      this.$emit("change");
    }
  },
  mounted() {
    this.$store.dispatch("requireExtraParams");
  }
};
</script>

<style>
</style>
