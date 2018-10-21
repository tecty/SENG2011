<template>
  <v-flex xs12 sm6>
    <v-select
      v-model="key"
      :items="keyList"
      label="Extra Requirement"
    />
    <v-select v-if="key" :items="valList">
    </v-select>

  </v-flex>

</template>

<script>
import { mapState } from 'vuex';

export default {
  data(){
    return {
      key:"",
      id:"",
    }
  },
  computed:{
    ...mapState({
      eps: (state)=> (state.extraParam.extraParameter),
      keyList: (state)=> {
        return Object.keys(state.extraParam.extraParameter);
      },
    }),
    valList(){
      if (this.key){
        return this.eps[this.key];
      }
      return []
    }
  },
  mounted(){
    this.$store.dispatch('requireExtraParams');
  }
}
</script>

<style>

</style>
