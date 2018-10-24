<template>
  <v-container full-height>
    <div v-if="api_state != 'READY' && api_state != 'ERROR'" class="text-xs-center">
      <v-progress-circular indeterminate color="primary" />
    </div>
    <div v-else>
      <!-- content of the post  -->
      <v-layout row wrap>
        <v-flex xs11>
          <h3 class="display-1 primary--text">
            <span class="grey--text">#{{ post.id }}</span> {{post.title}}
          </h3>
        </v-flex>
        <v-flex xs1 v-if="post.event.owner.username == username">
          <v-btn color="primary" :to="{
            name:'PostEdit',
            params: {
              postId:post.id,
            }
          }">Edit</v-btn>
        </v-flex>
      </v-layout>
      <p>{{ post.state | stateToText}}</p>
      <h5 class="headline primary--text ">Issuer:</h5>
      <p>{{ post.event.owner.username }}</p>
      <h5 class="headline primary--text ">Event Time:</h5>
      <p>{{ post.event.eventTime | showDateTime }}</p>
      <h5 class="headline primary--text ">Bid End:</h5>
      <p>{{ post.event.bidClosingTime | showDateTime }}</p>
      <h5 class="headline primary--text ">
        peopleCount
      </h5>
      <p>{{post.peopleCount}} </p>
      <h5 class="headline primary--text ">
        Budget
      </h5>
      <p>${{post.budget}}</p>
      <parmCard :criteria="post.extraParameter" />
      <h5 class="headline primary--text ">
        Message
      </h5>
      <msgBox :msg="post.msg" />
      <v-layout>
        <v-flex xs12>
          <h5 class="headline primary--text ">
            Bid
          </h5>
          <!-- select sorting parameter  -->
          <sortingSelector :sortBy="sortParameter" :list="bidsShow" @sorted="sortbidsShow" />
          <!-- cards of bids -->
          <div v-for="bid in bidsShow" :key="bid.id">
            <bid-card :bid="bid" :post="post" @requireRefresh="()=> refreshContent()" />
            <br/>
          </div>
          <!-- card for bidding -->
          <CreateCard v-if="canBid()" :postId="post.id" @requireRefresh="()=> refreshContent()" />
        </v-flex>
      </v-layout>
    </div>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import parmCard from "@/components/post/extraParm.vue";
import msgBox from "@/components/helper/messageBox.vue";
import sortingSelector from "@/components/helper/mergeSort.vue";
import BidCard from "@/components/bid/BidCard";
import CreateCard from "@/components/bid/CreateCard";

export default {
  data() {
    return {
      post: {},
      sortParameter: [
        "Lastest",
        "Sort by offer price",
        "Sort by bidder name",
        "Default"
      ]
    };
  },
  computed: {
    bidsShow: {
      get: function() {
        return this.post.bid_set;
      },
      // setter
      set: function(newList) {
        this.post.bid_set = newList;
      }
    },
    ...mapState({
      api_state: "api_state",
      username: state => state.username
    })
  },
  methods: {
    ...mapActions(["refreshAll", "getPostById"]),
    sortbidsShow(sortedList) {
      this.bidsShow = sortedList;
    },
    canBid() {
      return (
        this.api_state == "READY" &&
        this.post.event.owner.username != this.username &&
        this.post.state == "BD"
      );
    },
    refreshContent() {
      this.refreshAll().then(() => {
        // assign the new post object
        this.post = this.$store.state.posts.find(el => el.id == this.post.id);
        // declear the page is re-rendered
        this.$store.commit("API_READY");
      });
    }
  },
  mounted() {
    this.$store.dispatch("refreshAll").then(() => {
      this.post = this.$store.state.posts.find(el => {
        return el.id == this.$route.params.postId;
      });
      this.$store.commit("API_READY");
    });
  },
  components: {
    msgBox,
    BidCard,
    CreateCard,
    parmCard,
    sortingSelector
  },
  $_veeValidate: {
    validator: "new"
  }
};
</script>