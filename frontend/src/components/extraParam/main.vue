<template>
  <v-layout>
    <extraSelect v-for="i in count" :key="i"/>
  </v-layout>
</template>

<script>
import extraSelect from "./sub"
export default {
  data(){
    return {
      keys:[],
      count:1,
    }
  },
  methods:{

  },
  mounted(){
    this.$store.dispatch('requireExtraParams')
  },
  components: {
    extraSelect
  }
}
</script>

<style>

</style>
