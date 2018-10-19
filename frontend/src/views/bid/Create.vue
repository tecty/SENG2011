<template>
  <v-container>

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
      post: {}
    };
  },
  computed: mapState({
    "api_state": 'api_state',
    currUser: state => state.username,
  }),
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
