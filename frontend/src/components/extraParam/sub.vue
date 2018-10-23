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
      <v-select v-if="key" :items="valList" v-model="id" @change="declearChange" />
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  props: ["index", "value"],
  data() {
    return {
      key: "",
      id: ""
    };
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
    }
  },
  mounted() {
    this.$store.dispatch("requireExtraParams");
  }
};
</script>

<style>
</style>
