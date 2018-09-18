<template>
  <v-card>
    <v-card-title primary-title>
      <h4>{{post.title}}</h4>
    </v-card-title>
    <v-card-actions>
      <v-form fluid >
        <v-layout row wrap >
          <v-text-field v-model="offer"  ></v-text-field>
          <v-btn color="success" type="submit" >bid</v-btn>
        </v-layout>
      </v-form>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  // the data of this post
  props: ["post"],
  data() {
    return {
      offer: ""
    };
  }
};
</script>
