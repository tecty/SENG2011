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
        <msgCard :msg="bid.msg" />
       </v-card-text>
        <v-card-actions>
          <div v-if="post.event.owner.username == currUser && post.state == 'BD'">
            <v-btn flat dark @click="chooseBid()">Choose</v-btn>
          </div>
          <div v-if="bid.owner.username == currUser">
            <v-btn flat dark @click="deleteBid()">Delete</v-btn>
          </div>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import msgCard from "@/components/helper/messageBox.vue";
import { mapState, mapActions } from "vuex";
export default {
  // the data of this post
  props: ["value","index", "post"],
  data() {
    return {
      bid:{
        owner:{
          username:""
        }
      }
    };
  },
  computed: {
    ...mapState({
      currUser: "username"
    })
  },
  methods: {
    ...mapActions(["chooseBidById", "deleteBidById"]),
    chooseBid() {
      this.chooseBidById(this.post.id, this.bid.id).then(() => {
        this.$emit("requireRefresh");
      });
    },
    deleteBid() {
      this.deleteBidById(this.bid.id).then(() => {
        console.log("imhere")
        this.$emit("requireRefresh");
        console.log("after event emit")
      });
    }
  },
  components: {
    msgCard
  },
  mounted() {
    this.bid = this.value[this.index];
    console.log(this.bid)
  },
};
</script>
