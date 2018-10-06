<template>
  <v-card raised color="blue-grey lighten-2">
    <v-layout row wrap>
      <v-flex xs12>
        <v-card-title primary-title>
          <div>
            <span class="headline">Task detail of {{post.title}}</span><br>
            <span>{{post.message}}</span><br>

          </div>
          {{post.state}}
          <v-card-text>
            <span>Starting at: {{post.event.eventTime}}</span><br>
            <span>Bid will closes in: {{post.event.bidClosingTime}}</span>
          </v-card-text>
        </v-card-title>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn flat color="orange">Comment</v-btn>
        </v-card-actions>

      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  // the data of this post
  props: ["post"],
  data() {
    return {};
  }
};
</script>