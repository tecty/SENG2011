<template>
  
</template>

<script>
export default {
  data(){
    return {
      keys:[]
    }
  },
  methods:{

  },
  mounted(){
    this.$store.dispatch('requireExtraParams')
  }
}
</script>

<style>

</style>
