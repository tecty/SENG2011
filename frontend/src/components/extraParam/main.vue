<template>
  <v-layout column>
    <v-flex xs12>
      <!-- this array will have index +1 i don't knwo why -->
      <extraSelect 
        v-for="i in count" :key="i" :index="i-1"
        @change="declearChange"
      />
    </v-flex>
    <v-flex xs12 pa-0>
      <v-btn color="success" 
      @click="()=>{
        this.PUSH_EMPTY_SELECTED(); 
        this.declearChange()}">
        + More Extra Requirements
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import extraSelect from "./sub";
import { mapState, mapMutations } from "vuex";
export default {
  // this will accept the original value of extraparams
  props: ["value"],
  data() {
    return {
      keys: []
    };
  },
  computed: {
    ...mapState({
      selected: state => state.extraParam.selected
    }),
    count() {
      if (this.selected && this.selected.length > 0) {
        return this.selected.length;
      }
      return 0;
    }
  },
  methods: {
    ...mapMutations(["PUSH_EMPTY_SELECTED"]),
    declearChange() {
      // as the https://cn.vuejs.org/v2/guide/components.html
      // bind the new ids array to the input event
      this.$emit(
        "input",
        // i don't know why i can't use getter here.
        this.$store.state.extraParam.selected.filter(el => el != undefined)
      );
    }
  },
  mounted() {
    this.$store.dispatch("requireExtraParams");

    // assign the old selected from the post to vuex
    this.$store.commit("SET_SELECTED", this.value);
  },
  components: {
    extraSelect
  }
};
</script>

<style>
</style>
