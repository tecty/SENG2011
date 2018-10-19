<template>
  <v-container>
    <v-layout>
      <v-flex xs12 >
        <!-- cards of bids -->
        <div v-for="bid in post.bid_set" :key="bid.id">
          <bid-card :bid="bid" :post="post"></bid-card>
          <br/>
        </div>
        <!-- card for bidding -->
        <CreateCard v-if="canBid()"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";
import BidCard from "@/components/bid/BidCard";
import CreateCard from "@/components/bid/CreateCard";
export default {
  data() {
    return {
      // require a valid function.
      // here just for silence the error
      message: "",
      price: "",
      error: "",
      currUser: localStorage.getItem("username"),
      post: {}
    };
  },
  computed: mapState(["api_state"]),
  mounted() {
    this.$store.dispatch("requireExtraParams");
    this.$store
      .dispatch("refreshAll")
      .then(() =>
        this.$store.dispatch("getPostById", this.$route.params.postId)
      )
      .then(res => {
        this.post = res;
      });
  },
  methods: {
    ...mapActions([ "refreshPosts"]),
    canBid:() => (
      true || 
      this.post.event.owner.username != currUser && 
      this.post.state == 'BD'
    )
  },
  components: {
    BidCard,
    CreateCard
  },
  $_veeValidate: {
    validator: "new"
  }
};
</script>
