<template>
  <v-card>
    <v-card-text>
      <form @submit.prevent="submit">
        <v-text-field v-validate="'required|decimal:3'" data-vv-name="price" 
          v-model="price" label="Price"
          :error-messages="errors.collect('price')" required />
        <v-textarea v-model="message" v-validate="'required'" 
          data-vv-name="message" label="Message" 
          hint="Leave a message to help you win the bid."
          :error-messages="errors.collect('message')" required />        
        <v-btn type="submit" color="success">Bid</v-btn>
      </form>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: ["postId"],
  data() {
    return {
      price: "",
      message: "",
      error: {}
    };
  },
  computed: {},
  methods: {
    ...mapActions(["placeBid"]),
    submit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          var data = {
            post: this.$route.params.postId,
            offer: this.price,
            message: this.message
          };
          this.placeBid(data)
            .then(() => {
              this.$emit("requireRefresh");
            })
            .catch(err => {
              this.error = err;
            });
        }
      });
    }
  }
};
</script>
