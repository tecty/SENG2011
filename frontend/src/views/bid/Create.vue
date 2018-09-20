<template>
 <v-layout>
    <v-flex xs12 sm6 offset-sm3>
        <!-- card  for the detail of the post -->
        <post-detail-card :post="post" />
      <v-card>


        <!-- cards of bids -->
           <v-card>
      <v-container
        fluid
        grid-list-lg
      >
  <bid-card v-for="bid in post.bid_set" :key="bid.id" :bid="bid"></bid-card>
        </v-container>
    </v-card>
      <!-- card for making post -->
      <v-card>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        v-model="price"
        label="Price"
        
        required
      
      ></v-text-field>
      <v-textarea
        v-model="message"
        label="Message"
        hint="Write Message to poster in your bid"
        required
      
      ></v-textarea>
      <v-btn type="submit" color="primary">Bid</v-btn>
    </v-form>
      </v-card>
    
  </v-card>
    </v-flex>
  </v-layout>

</template>

<script>
import { mapActions } from "vuex";
import PostDetailCard from "@/components/PostDetailCard";
import BidCard from "@/components/BidCard";
export default {
  data() {
    return {
      // require a valid function.
      // here just for silence the error
      valid: true,
      price: "",
      error: "",
    };
  },
  computed: {
    post: function() {
      return this.$store.state.posts[this.$route.params.postId-1]
    }
  },
  methods: {
    ...mapActions(["placeBid"]),
    submit() {
      if (this.$refs.form.validate()) {
        var data = {
          post: this.$route.params.postId,
          offer: this.price
        };
        console.log(data);
        console.log(this.$route.params.postId);
        this.placeBid(data)
          .then(() => {
            this.$router.next("/");
          })
          .catch((err) => {
            this.error = "import is not correct";
            console.log(err);
            console.log(err.response);
            console.log(err.response.data);
          });
      }
    },
  },
  components: {
    PostDetailCard,
    BidCard
  }
};
</script>
