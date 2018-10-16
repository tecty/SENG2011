<template>
  <v-container fluid grid-list-md>
    <v-data-iterator :items="posts" content-tag="v-layout" row wrap>
      <v-flex slot="item" slot-scope="props" sm12 sm6 md4 lg3 >
        <!-- actual data is iterating at this v-flex layer -->
        <postCard :post="props.item"/>
      </v-flex>
    </v-data-iterator>
      <v-btn fixed bottom right fab dark color="red" to="/post/create">
      <v-icon dark>add</v-icon>
    </v-btn>
  </v-container>
</template>


<script>
import postCard from "@/components/post/Card";
export default {
  computed: {
    posts() {
      return this.$store.state.posts;
    }
  },
  components: {
    postCard
  }
};
</script>

<style scoped>
</style>
