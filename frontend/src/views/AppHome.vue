<template>
  <v-jumbotron
    :gradient="gradient"
    dark
    src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
  >
    <v-container fill-height>
      <v-layout align-center>
        <v-flex>
          <h3 class="display-3">Welcome to the PartyWhip</h3>

          <span class="subheading">Lorem ipsum dolor sit amet, pri veniam forensibus id. Vis maluisset molestiae id, ad semper lobortis cum. At impetus detraxit incorrupte usu, repudiare assueverit ex eum, ne nam essent vocent admodum.</span>

          <v-divider class="my-3"></v-divider>

          <div class="title mb-3">Check out our newest features!</div>

          <v-btn
            class="mx-0"
            color="primary"
            large
          >
            See more
          </v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-jumbotron>
</template>


<script>
export default {
  data: () => ({
    gradient: "to top right, rgba(63,81,181, .7), rgba(25,32,72, .7)"
  })
};
</script>

<style scoped>
</style>
