<template>
  <div>
    <v-form v-model="valid" @submit.prevent="submit">
      <v-text-field
        v-model="price"
        label="Price"
        required
      ></v-text-field>
      {{this.$route.params}}  {{this.$route.name}}
      <v-btn type="submit" color="primary">Bid</v-btn>
    </v-form>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      // require a valid function.
      // here just for silence the error
      valid: "",
      price: "",
      error: ""
    };
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
    }
  }
};
</script>
