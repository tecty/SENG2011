<template>
 <v-layout>
    <v-flex xs12 sm6 offset-sm3>
        <!-- card  for the detail of the post -->
        <post-detail-card :post="post" />
      <v-card>
      <!-- card for making post -->
    <v-form v-model="valid" @submit.prevent="submit">
      <v-text-field
        v-model="price"
        label="Price"
        required
      ></v-text-field>
      <v-btn type="submit" color="primary">Bid</v-btn>
    </v-form>
  </v-card>
    </v-flex>
  </v-layout>

</template>

<script>
import { mapActions } from "vuex";
import PostDetailCard from "@/components/PostDetailCard";
export default {
  data() {
    return {
      // require a valid function.
      // here just for silence the error
      valid: "",
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
        .catch(() => {
          this.error = "import is not correct";
        });
    },
    getPost(){
      
    }
  },
  components: {
    PostDetailCard
  }
};
</script>
