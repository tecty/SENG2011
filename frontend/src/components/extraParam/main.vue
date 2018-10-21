<template>
  <v-layout column>
    <v-flex xs12>
      <extraSelect v-for="i in count" :key="i"  :index="i" @change ="declearChange"/>
    </v-flex>
    <v-flex xs12 pa-0>
      <v-btn color="success" @click="addCount">+ More Extra Requirements</v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import extraSelect from "./sub"
export default {
  // this will accept the original value of extraparams
  props:['value'],
  data(){
    return {
      keys:[],
      count:1,
    }
  },
  methods:{
    addCount(){
      this.count ++;
    },
    declearChange(){
      // as the https://cn.vuejs.org/v2/guide/components.html
      // bind the new ids array to the input event 
      this.$emit('input', 
        this.$store.state.extraParam.selected
          .filter(el=>el!= undefined)
      );
    }
  },
  mounted(){
    this.$store.dispatch('requireExtraParams');
    // clear all the selected param id 
    this.$store.commit('CLEAR_SELECTED');
  },
  components: {
    extraSelect
  }
}
</script>

<style>

</style>
