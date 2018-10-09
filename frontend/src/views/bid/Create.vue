<template>
  <v-container>
    <v-flex xs12 sm6 offset-sm3>
      <!-- card  for the detail of the post -->
      <post-detail-card :post="post" />
      <v-card>
        <!-- cards of bids -->
        <v-card>
          <v-container fluid grid-list-lg>
            <bid-card v-for="bid in post.bid_set" :key="bid.id" :bid="bid" :post="post"></bid-card>
          </v-container>
        </v-card>
        <!-- card for making post -->
        <div v-if="post.event.owner.username != currUser && post.state == 'BD'">
          <v-card>
            <form @submit.prevent>
              <v-text-field v-validate="'required|decimal:3'" data-vv-name="price" v-model="price" label="Price" :error-messages="errors.collect('price')"
                required></v-text-field>
              <v-textarea v-model="message" v-validate="'required'" data-vv-name="message" label="Message" hint="Write Message to poster in your bid"
                :error-messages="errors.collect('message')" required></v-textarea>
              <v-btn type="submit" color="primary" @click="submit">Bid</v-btn>
            </form>
          </v-card>
        </div>
        </v-card>
        
    </v-flex>
  </v-container>
</template>

<script>
import { mapActions, mapState, mapGetters } from "vuex";
import PostDetailCard from "@/components/PostDetailCard";
import BidCard from "@/components/BidCard";
export default {
  data() {
    return {
      // require a valid function.
      // here just for silence the error
      message: "",
      price: "",
      error: "",
      currUser: localStorage.getItem("username")
    };
  },
  computed: mapState({
    // arrow functions can make the code very succinct!
    posts: state => state.posts,

    // passing the string value 'posts' is same as `state => state.count`
    postsAlias: "posts",

    // to access local state with `this`, a normal function must be used
    post(state) {
      return state.posts.find(post => post.id == this.$route.params.postId - 1);
    }
  }),
  // computed: {
  //   ...mapGetters({
  //     post: "currPost"
  //   })
  // },
  //   post: function() {
  //     return this.$store.state.posts[this.$route.params.postId - 1];
  //   }
  // },
  methods: {
    ...mapActions(["placeBid", "addPosts"]),
    submit() {
      this.$validator.validateAll().then(valid => {
        if (valid) {
          var data = {
            post: this.$route.params.postId,
            offer: this.price,
            message: this.message
          };
          console.log(data);
          console.log(this.$route.params.postId);
          this.placeBid(data)
            .then(response => {
              this.addPosts();
              console.log(response);
            })
            .catch(err => {
              this.error = "import is not correct";
              console.log(err);
            });
        }
      });
    }
  },
  components: {
    PostDetailCard,
    BidCard
  },
  $_veeValidate: {
    validator: "new"
  }
};
</script>