<template>
  <div class="ml-0 mr-4 mb-2">
      <v-card color="blue-grey darken-2" class="white--text">
        <v-card-title primary-title>
          <span class="headline">
            ${{bid.offer}} | {{ bid.state | stateToText }}
          </span>
          <v-spacer />
          <router-link :to="{
            name:'ProfileDetail',
            params: {
              user:post.event.owner
            }
          }">
            <span>by {{bid.owner.username}} </span>
          </router-link>
          <i class="material-icons ml-2">star</i>{{ bid.rateOfBidder }}
        </v-card-title>
       <v-card-text>
        <msgCard :msg="bid.msg" />
       </v-card-text>
        <v-card-actions>
          <div v-if="isPoster">
            <v-btn v-if="bid.state == 'BD'"
              flat dark @click="chooseBid">
                Choose
            </v-btn>
            <v-btn v-if="bid.state == 'SD'"
              flat dark @click="finishBid">
                Finished
            </v-btn>
            <div v-if="bid.state == 'FN'" class="ml-2">
              <star-rating  v-model="rate" @click="finishBid" 
                :read-only="! canRate" :star-size="23" 
                :padding="1" :show-rating="false" :inline="true"/>
              <v-btn v-if="canRate" flat dark @click="SendRateOfBidder">Rate</v-btn>
            </div>
          </div>
          <div v-if="isDeletable">
            <v-btn flat dark @click="deleteBid">Delete</v-btn>
          </div>
        </v-card-actions>
      </v-card>
  </div>
</template>

<script>
import msgCard from "@/components/helper/messageBox.vue";
import StarRating from "vue-star-rating";

import { mapState, mapActions } from "vuex";
export default {
  // the data of this post
  props: ["bid", "post"],
  data() {
    return {
      // one of the rate box will bind to this property
      tmpRate: 0
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
    },
    canRate() {
      return (
        // can rate by poster
        this.bid.bidderReceivedPoints == 0 &&
        // or can rate by bidder
        this.post.posterReceivedPoints == 0
      );
    },
    rate: {
      get() {
        if (this.canRate) {
          return this.tmpRate;
        }
        // if this bidder have receive the point,
        // then alway show the received point
        return this.bid.bidderReceivedPoints;
      },
      set(newVal) {
        if (this.canRate) {
          // if this bid can rate, then se
          this.tmpRate = newVal;
        }
      }
    }
  },
  methods: {
    ...mapActions([
      "chooseBidById",
      "deleteBidById",
      "finishBidById",
      "rateBidder"
    ]),
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
      this.finishBidById(this.post.id).then(() => {
        this.$emit("requireRefresh");
      });
    },
    SendRateOfBidder() {
      if (this.canRate && this.rate != 0) {
        // rate should be selected
        this.rateBidder({
          postId: this.post.id,
          rate: this.rate
        }).then(() => {
          this.$emit("requireRefresh");
        });
      }
    }
  },
  components: {
    msgCard,
    StarRating
  },
  mounted() {}
};
</script>

<style scoped>
a {
  color: white;
}
</style>
