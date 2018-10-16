<template>
  <v-container fluid grid-list-md>
    <v-data-iterator :items="events"
      content-tag="v-layout" row wrap
      v-if="api_state != 'WAIT'"
    >
      <v-flex slot="item" slot-scope="props" sm12 sm6 md4 lg3 >
        <!-- actual data is iterating at this v-flex layer -->
        <eventCard :event="props.item"/>
      </v-flex>
    </v-data-iterator>
      <v-btn fixed bottom right fab dark color="red" to="/event/create">
      <v-icon dark>add</v-icon>
    </v-btn>
  </v-container>
  
</template>


<script>
import EventCard from "@/components/event/Card";
import { mapState } from 'vuex';
export default {
  computed: mapState(['events','api_state']),
  mounted() {
    // fetch the latest events 
    this.$store.dispatch("refreshAll");
  },
  components: {
    EventCard
  }
};
</script>

<style scoped>
</style>
