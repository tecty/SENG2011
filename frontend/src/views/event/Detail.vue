<template>
  <v-container>
    <div v-if="api_state == 'READY'">
      <!-- content of the event  -->
      <v-layout row wrap>
        <v-flex xs11>
          <h3 class="display-1 primary--text">
            <span class="grey--text">#{{ event.id }}</span> {{event.title}}
          </h3>
        </v-flex>
        <v-flex xs1 v-if="event.owner.username == username">
          <v-btn color="primary" :to="{
            name:'EventEdit',
            params: {
              eventId:event.id,
            }
          }">Edit</v-btn>
        </v-flex>
      </v-layout>
      <h5 class="headline primary--text ">Owner:</h5>
      <p>{{ event.owner.username }}</p>
      <h5 class="headline primary--text ">
        Location
      </h5>
      <p>{{event.location.address}}</p>
      <h5 class="headline primary--text ">
        Event Time
      </h5>
      <p>{{event.eventTime | showDateTime }}</p>
      <h5 class="headline primary--text ">
        Bid Closing Time
      </h5>
      <p>{{event.bidClosingTime | showDateTime }}</p>
    </div>
    <div class="text-xs-center" v-else>
      <v-progress-circular indeterminate color="primary" />
    </div>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      event: {}
    };
  },
  computed: {
    ...mapState(["api_state", "username", "posts"])
  },
  mounted() {
    this.$store.dispatch("requireExtraParams");

    this.$store
      .dispatch("getEventById", this.$route.params.eventId)
      .then(res => {
        this.event = res.data;
        this.$store.commit("API_READY");
      });
  }
};
</script>
