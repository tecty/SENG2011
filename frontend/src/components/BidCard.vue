<template>

  <v-layout row wrap>
    <v-flex xs12>
      <v-card color="blue-grey darken-2" class="white--text">
        <v-card-title primary-title>
          <span class="headline">{{bid.owner.username}}</span>
          <br><v-spacer></v-spacer>
          <span> offer ${{bid.offer}}</span>
        </v-card-title>
        <v-card-actions>
          <div v-if="post.event.owner.username == currUser">
            <v-btn flat dark @click="updatePostStatus()">Choose</v-btn>
          </div>
          <v-spacer></v-spacer>
          <v-btn flat color="orange">Comment</v-btn>
        </v-card-actions>
      </v-card>
          {{this.post}}
    </v-flex>
  </v-layout>

</template>

<script>
import { mapActions, mapState } from "vuex";
  export default {
    // the data of this post
    props: ["bid", "post"],
    data() {
      return {
        currUser: localStorage.getItem("username")
      };
    },
    methods: {
      ...mapActions(["updatePost"]),
      updatePostStatus() {
        this.post.state = "SD"; // bidding => selected
        // var data = {
        //   id: this.post.id,
        //   title: this.post.title,
        //   message: this.post.message,
        //   budget: this.post.budget,
        //   peopleCount: this.post.peopleCount,
        //   extraParameter: this.post.extraParameter // TODO extraparameter
        // }
        axios
        .patch("posts/" + this.post.id + "/", {state: "SD"})
          .then(response => {
            // JSON responses are automatically parsed.
            console.log(response);
            console.log(response.data);
          })
          .catch(error => {
            console.log(error);
            console.log(error.response);
          });
      //   this.updatePost(this.post.id,this.post)
      //   .then((response) => {
      //           console.log(response);
      //         })
      //         .catch((err) => {
      //           this.error = "import is not correct";
      //           console.log(err);
      //         });
      // }
      }
    },
  };
</script>