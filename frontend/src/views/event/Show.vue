<template>
  <v-container fluid grid-list-md>
      <sortingSelector :sortBy="sortParameter" :list="events" @sorted="sortEvents"/>
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
import sortingSelector from "@/components/helper/mergeSort.vue";
import EventCard from "@/components/event/Card";
import { mapState } from "vuex";
export default {
  data() {
    return {
      sortParameter: [
        "Sort by Bid Ending time",
        "Sort by Event time",
        "Sort by Number of Posts under an Event",
        "Sort by Event owner Name",
        "Default"
      ]
    };
  },
  computed: {
    events: {
      get() {
        return this.$store.state.events;
      },
      set(newList) {
        return this.$store.commit("SET_EVENTS", newList);
      }
    },
    ...mapState(["api_state"])
  },
  methods: {
    sortEvents(list) {
      this.events = list;
    }
  },
  mounted() {
    // fetch the latest events
    this.$store.dispatch("refreshAll");
  },
  components: {
    EventCard,
    sortingSelector
  }
};
</script>

<style scoped>
</style>
