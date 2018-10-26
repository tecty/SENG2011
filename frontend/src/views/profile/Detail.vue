<template>
  <v-container full-height>
    <v-layout row wrap>
      <h3 class="display-1 primary--text">
        <span class="grey--text">#{{ user.id }}</span> {{ user.username }}
      </h3>
      <v-spacer></v-spacer>
      <h3 v-if="user.is_trusted" class="headline success--text">
        Trusted User
      </h3>
      <h3 v-else class="headline grey--text">
        No Verified User
      </h3>
    </v-layout>
    <h5 class="headline primary--text ">Address:</h5>
    <p>{{ user.location.address }}</p>
    <h5 class="headline primary--text ">Telephone:</h5>
    <p>{{ user.tel }}</p>
  </v-container>
</template>

<script>
export default {
  data(){
    return {
      user:{}
    };
  },
  mounted() {
    // fetch the data from api route
    // hence, in this way, we wont have another
    //  request to server
    this.user = this.$route.params.user;
  },
};
</script>

<style>
</style>
