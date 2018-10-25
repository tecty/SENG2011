<template>
  <v-container fluid grid-list-md>
    <v-flex xs12 sm8 md6 lg3>
      <sortingSelector v-model="events" :sortBy="sortParameter" />
    </v-flex>
    <v-data-iterator :items="events"
      content-tag="v-layout" row wrap
      :rows-per-page-items="[12]"
      v-if="api_state == 'READY'"
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
      events:[],
      sortParameter: [
        {
          text: "Bid Ending time",
          value: {
            id: 1,
            f: (a, b) =>
              Date.parse(a.bidClosingTime) - Date.parse(b.bidClosingTime)
          }
        },
        {
          text: "Event time",
          value: {
            id: 2,
            f: (a, b) => Date.parse(a.eventTime) - Date.parse(b.eventTime)
          }
        },
        {
          text: "Number of Posts under an Event",
          value: {
            id: 3,
            f: (a, b) => a.post_set.length - b.post_set.length
          }
        },
        {
          text: "Event owner Name",
          value: {
            id: 4,
            f: (a, b) => a.owner.username.localeCompare(b.owner.username)
          }
        },
        {
          text: "Default",
          value: {
            id: 5,
            f: (a, b) => a.id - b.id
          }
        }
      ]
    };
  },
  computed: {
    ...mapState(["api_state"])
  },
  methods: {
  },
  mounted() {
    // fetch the latest events
    this.$store.dispatch("refreshAll").then(()=>{ 
      this.events = this.$store.state.events;
      this.$store.commit('API_READY');
    });
  },
  components: {
    EventCard,
    sortingSelector
  }
};
</script>

<style scoped>
</style>
