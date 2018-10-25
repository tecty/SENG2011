<template>
  <v-container full-height>
    <div v-if="api_state != 'READY' && api_state != 'ERROR'" class="text-xs-center">
      <v-progress-circular indeterminate color="primary" />
    </div>
    <div v-else>
      <v-layout row wrap>
        
      </v-layout>
    </div>
  </v-container>
</template>

<script>
export default {

}
</script>

<style>

</style>
