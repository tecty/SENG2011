<template>
  <v-container fluid grid-list-md>
    <!-- select sorting parameter  -->
    <sortingSelector :sortBy="sortParameter" :list="posts" @sorted="sortPosts" />

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
        "Sort by Bid Ending time",
        "Sort by Event time",
        "Sort by Budget",
        "Sort by Number of bids",
        "Sort by issuer name",
        "Sort by Number of people",
        "Default"
      ]
    };
  },
  computed: {
    posts: {
      get() {
        return this.$store.state.posts;
      },
      set(newList) {
        return this.$store.commit("SET_POSTS", newList);
      }
    },
    ...mapState(["api_state"])
  },

  methods: {
    sortPosts(list) {
      this.posts = list;
    }
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