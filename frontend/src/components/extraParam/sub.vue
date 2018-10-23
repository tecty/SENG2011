<template>
  <v-layout row fill-height>
    <v-flex xs12 sm6>
      <!-- selection of the key  -->
      <v-select
        v-model="key"
        :items="keyList"
        label="Extra Requirement"
      />
    </v-flex >
    <v-flex xs12 sm6>
      <!-- selection of the value -->
      <v-select v-if="key" :items="valList" v-model="id" @change="declearIdChange" />
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  props: ["index"],
  data() {
    return {
      key: "",
      id: ""
    };
  },
  methods: {
    ...mapMutations(["ADD_SELECTED"]),
    declearKeyChange() {
      // revoke the selected id
      this.id = undefined;
      // add this selected id
      this.ADD_SELECTED({
        index: this.index,
        id: this.id
      });
      // emit a changed event
      this.$emit("change");
    },
    declearIdChange() {
      // add this selected id
      this.ADD_SELECTED({
        index: this.index,
        id: this.id
      });
      // emit a changed event
      this.$emit("change");
    }
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
        let ret = this.eps[this.key];
        ret.unshift({ value: null, text: "removed" });
        return ret;
      }
      return [];
    }
  },
  mounted() {
    this.id = this.$store.state.extraParam.selected[this.index];
    if (this.id != undefined) {
      this.$store
        .dispatch("getEpById", this.id)
        .then(ep => (this.key = ep.key));
    }
    // reset the key to mek the revoke id in key work
    this.id = this.$store.state.extraParam.selected[this.index];
  }
};
</script>

<style>
</style>
