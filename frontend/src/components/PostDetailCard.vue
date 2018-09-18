<template>
  <v-card>
    <v-card-title primary-title>
          <div>
            {{post.title}}
          </div>
        </v-card-title>

        <v-card-actions>
          <v-btn flat color="orange">Share</v-btn>
          <v-btn flat color="orange">Explore</v-btn>
        </v-card-actions>

  </v-card>
</template>

<script>
export default {
  // the data of this post
  props: ["post"],
  data() {
    return {
    };
  }
};
</script>
