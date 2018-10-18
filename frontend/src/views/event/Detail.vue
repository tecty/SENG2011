<template>
  <v-container>
    <div v-if="api_state == 'READY'">
      <!-- content of the event  -->
      <h3 class="display-1 primary--text">
        <span class="grey--text">#{{ event.id }}</span> {{event.title}}
      </h3>
      <h5 class="headline primary--text ">
        Location
      </h5>{{event.location.address}} 
      <h5 class="headline primary--text ">
        Event Time
      </h5>{{event.eventTime}} 
      <h5 class="headline primary--text ">
        Bid Closing Time
      </h5>{{event.bidClosingTime}} 
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
  computed: mapState(["api_state"]),
  mounted() {
    this.$store.dispatch("requireExtraParams");
    this.$store
      .dispatch("refreshAll")
      .then(() =>
        this.$store.dispatch("getEventById", this.$route.params.eventId)
      )
      .then(res => {
        this.event = res;
        this.$store.commit("API_READY");
      });
  }
};
</script>
