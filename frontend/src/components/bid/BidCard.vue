<template>
  <v-layout row wrap mb-3>
    <v-flex xs12>
      <v-card color="blue-grey darken-2" class="white--text">
        <v-card-title primary-title>
          <span class="headline">
            ${{bid.offer}} | {{ bid.state | stateToText }}
          </span>
          <v-spacer />
          <span>by {{bid.owner.username}} </span>
          <i class="material-icons ml-2">star</i>{{ bid.rateOfBidder }}
        </v-card-title>
       <v-card-text>
        <msgCard :msg="bid.msg" />
       </v-card-text>
        <v-card-actions>
          <div v-if="isPoster">
            {{bid.state}}
            <v-btn v-if="bid.state == 'BD'" flat dark @click="chooseBid">Choose</v-btn>
            <v-btn v-if="bid.state == 'SD'" flat dark @click="finishBid">Finished</v-btn>
            <v-btn v-if="bid.state == 'FN'" flat dark @click="finishBid">Finished</v-btn>
          </div>
          <div v-if="isDeletable">
            <v-btn flat dark @click="deleteBid">Delete</v-btn>
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
  props: ["bid", "post"],
  data() {
    return {
      // one of the rate box will bind to this property
      rate: 0
    };
  },
  computed: {
    ...mapState({
      currUser: "username"
    }),
    isDeletable() {
      return this.bid.owner.username == this.currUser && this.bid.state == "BD";
    },
    isPoster() {
      return this.post.event.owner.username == this.currUser;
    }
  },
  methods: {
    ...mapActions(["chooseBidById", "deleteBidById", "finishBidById"]),
    chooseBid() {
      this.chooseBidById({
        postId: this.post.id,
        bidId: this.bid.id
      }).then(() => {
        this.$emit("requireRefresh");
      });
    },
    deleteBid() {
      this.deleteBidById(this.bid.id).then(() => {
        this.$emit("requireRefresh");
      });
    },
    finishBid() {
      this.finishBidById({
        postId: this.post.id,
        bidId: this.bid.id
      }).then(() => {
        this.$emit("requireRefresh");
      });
    }
  },
  components: {
    msgCard
  },
  mounted() {}
};
</script>
