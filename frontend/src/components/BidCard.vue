<template>

  <v-layout row wrap>
    <v-flex xs12>
      <v-card color="blue-grey darken-2" class="white--text">
        <v-card-title primary-title>
          <span class="headline">{{bid.owner.username}}</span>
          <br><v-spacer></v-spacer>
          <span> offer ${{bid.offer}}</span>
        </v-card-title>
       <v-card-text>
        <div>message : {{bid.msg.msg}}</div>
       </v-card-text>
        <v-card-actions>
          <div v-if="post.event.owner.username == currUser && post.state == 'BD'">
            <v-btn flat dark @click="chooseBid()">Choose</v-btn>
          </div>
          <div v-if="bid.owner.username == currUser">
            <v-btn flat dark @click="deleteBid()">Delete</v-btn>
          </div>
          <v-spacer></v-spacer>
          <v-btn flat color="orange">Comment</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  // the data of this post
  props: ["bid", "post"],
  data() {
    return {};
  },
  computed:{
    ...mapState({
      currUser: 'username'
    })
  },
  methods: {
    chooseBid() {
      axios
        .post("posts/" + this.post.id + "/choose/", { id: this.bid.id })
        .then(response => {
          // JSON responses are automatically parsed.
          console.log(response);
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
          console.log(error.response);
        });
    },
    deleteBid() {
      axios
        .delete("bids/" + this.bid.id + "/")
        .then(response => {
          // JSON responses are automatically parsed.
          console.log(response);
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
          console.log(error.response);
        });
    }
  }
};
</script>