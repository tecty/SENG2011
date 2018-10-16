<template>

  <v-layout row wrap>
    <v-flex xs12>
      <v-card color="blue-grey darken-2" class="white--text">
        <v-card-title primary-title>
          <span class="headline">{{bid.owner.username}}</span>
          <br><v-spacer></v-spacer>
          <span> offer ${{bid.offer}}</span>
        </v-card-title>
        <v-card-actions>
          <v-btn flat dark>Choose</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>

</template>

<script>
  export default {
    // the data of this post
    props: ["bid"],
    data() {
      return {};
    }
  };
</script>