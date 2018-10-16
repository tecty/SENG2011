<template>
  <v-card raised color="blue-grey lighten-2">
    <v-layout row wrap>
      <v-flex xs12>
        <v-card-title primary-title>
          <div>
            <span class="headline">Task detail of {{event.title}}</span><br>
          </div>
          <v-card-text>
            <span>Starting at: {{event.eventTime}}</span><br>
            <span>Bid will closes in: {{event.bidClosingTime}}</span>
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
  // the data of this event
  props: ["event"],
  data() {
    return {};
  }
};
</script>
