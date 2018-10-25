<template>
  <v-container fluid grid-list-md>
      <v-data-iterator :items="posts" 
        content-tag="v-layout" row wrap
        v-if="api_state != 'WAIT'"
        :rows-per-page-items="[12]"
      >
        <v-flex slot="item" slot-scope="props" sm12 sm6 md4 lg3 >
          <!-- actual data is iterating at this v-flex layer -->
          <postCard :post="props.item"/>
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
import { mapState } from "vuex";
export default {
  computed: mapState(["posts", "api_state"]),
  mounted() {
    // fetch the latest posts
    this.$store.dispatch("refreshAll");
  },
  components: {
    postCard
  }
};
</script>

<style scoped>
</style>
