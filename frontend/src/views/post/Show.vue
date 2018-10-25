<template>
  <v-container fluid grid-list-md>
    <v-flex xs12 sm8 md6 lg3>
      <!-- select sorting parameter  -->
      <sortingSelector v-model="posts" :sortBy="sortParameter" />
    </v-flex>
    <v-data-iterator :items="posts" content-tag="v-layout" row wrap v-if="api_state != 'WAIT'">
      <v-flex slot="item" slot-scope="props" sm12 sm6 md4 lg3>
        <!-- actual data is iterating at this v-flex layer -->
        <postCard :post="props.item" />
      </v-flex>
    </v-data-iterator>
    <div class="text-xs-center" v-else>
      <v-progress-circular indeterminate color="primary" />
    </div>
    <v-btn fixed bottom right fab dark color="red" to="/post/create">
      <v-icon dark>add</v-icon>
    </v-btn>
  </v-container>
</template>


<script>
import postCard from "@/components/post/Card";
import sortingSelector from "@/components/helper/mergeSort.vue";

import { mapState } from "vuex";
export default {
  data() {
    return {
      sortParameter: [
        {
          text: "Bid Ending time",
          value: {
            id: 0,
            f: (a, b) =>
              Date.parse(a.event.bidClosingTime) -
              Date.parse(b.event.bidClosingTime)
          }
        },
        {
          text: "Event Time",
          value: {
            id: 1,
            f: (a, b) =>
              Date.parse(a.event.eventTime) - Date.parse(b.event.eventTime)
          }
        },
        {
          text: "Budget",
          value: {
            id: 2,
            f: (a, b) => parseInt(a.budget, 10) - parseInt(b.budget, 10)
          }
        },
        {
          text: "Number of Bids",
          value: {
            id: 3,
            f: (a, b) => a.bid_set.length - b.bid_set.length
          }
        },
        {
          text: "Issuer Name",
          value: {
            id: 4,
            f: (a, b) =>
              a.event.owner.username.localeCompare(b.event.owner.username)
          }
        },
        {
          text: "Number of People",
          value: {
            id: 5,
            f: (a, b) => a.peopleCount - b.peopleCount
          }
        },
        { text: "Default", value: { id: 6, f: (a, b) => a.id - b.id } }
      ]
    };
  },
  computed: {
    ...mapState(["api_state","posts"])
  },
  mounted() {
    // fetch the latest posts
    this.$store.dispatch("refreshAll");
  },
  components: {
    postCard,
    sortingSelector
  }
};
</script>

<style scoped>
</style>
