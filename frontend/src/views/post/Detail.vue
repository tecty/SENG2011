<template>
  <v-container full-height>
    <div v-if="api_state != 'READY'" class="text-xs-center">
      <v-progress-circular indeterminate color="primary" />
    </div>
    <div v-else>
      <!-- content of the post  -->
      <h3 class="display-1 primary--text">
        <span class="grey--text">#{{ post.id }}</span> {{post.title}}
      </h3>
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
      <msgBox :msg="post.msg" @requireRefresh="()=> {
        refreshContent()}" />
    </div>
    <v-layout>
      <v-flex xs12 >
        <h5 class="headline primary--text ">
          Bid
        </h5>
        <!-- sort buttons -->
      <div>
        <v-select
          :items="sortBy"
          label="Sort bids by"
          @change="selecteSortBy"
        ></v-select>
      </div>
        <!-- cards of bids -->
        <div v-for="bid in bidsShow" :key="bid.id">
          <bid-card :bid="bid" :post="post" 
            @requireRefresh="()=> refreshContent()" />
          <br/>
        </div>
        <!-- card for bidding -->
        <CreateCard v-if="canBid()" :postId="post.id" 
        @requireRefresh="()=> refreshContent()" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import parmCard from "@/components/post/extraParm.vue";
import msgBox from "@/components/helper/messageBox.vue";
import BidCard from "@/components/bid/BidCard";
import CreateCard from "@/components/bid/CreateCard";

export default {
  data() {
    return {
      post: {},
      sortBy: [
        "Lastest",
        "Sort by offer price",
        "Sort by bidder name",
        "Default"
      ],
      selectVal: ""
    };
  },
  computed: {
    bidsShow() {
      var compareFunc = (a, b) => {
        return a.id - b.id;
      };
      switch (this.selectVal) {
        case "Sort by offer price":
          compareFunc = (a, b) => {
            return parseInt(a.price, 10) - parseInt(b.price, 10);
          };
          break;
        case "Lastest":
          compareFunc = (a, b) => {
            return a.id - b.id;
          };
          break;
        case "Sort by bidder name":
          compareFunc = (a, b) => {
            return a.owner.username.localeCompare(b.owner.username);
          };
          break;
        default:
          return this.post.bid_set;
          break;
      }
      return this.mergeSort(this.post.bid_set, compareFunc);
    },
    ...mapState({
      api_state: "api_state",
      currUser: state => state.username
    })
  },
  methods: {
    ...mapActions(["refreshAll", "getPostById"]),
    canBid() {
      return (
        this.api_state == "READY" &&
        this.post.event.owner.username != this.currUser &&
        this.post.state == "BD"
      );
    },
    refreshContent() {
      this.refreshAll()
        .then(() => this.getPostById(this.$route.params.postId))
        .then(post => {
          // assign the new post object
          this.post = post;
          // declear the page is re-rendered
          this.$store.commit("API_READY");
        });
    },
    selecteSortBy(label) {
      console.log(label);
      this.selectVal = label;
    },
    mergeSort(list, compareFunc) {
      var temp = this.mergeSortRecu(list, 0, list.length - 1, compareFunc);
      return temp;
    },
    mergeSortRecu(list, lo, hi, compareFunc) {
      var newList = list.slice();
      if (lo < hi) {
        var mid = Math.floor((lo + hi) / 2);
        newList = this.mergeSortRecu(list, lo, mid, compareFunc);
        newList = this.mergeSortRecu(newList, mid + 1, hi, compareFunc);
        newList = this.merge(newList, lo, mid, hi, compareFunc);
      }
      return newList;
    },
    merge(newList, lo, mid, hi, compareFunc) {
      var buffer = newList.slice();
      // console.log(buffer);
      var i = lo;
      var j = mid + 1;
      var k = 0;
      while (k < hi - lo + 1) {
        if (i > mid) {
          buffer[lo + k] = newList[j];
          j++;
        } else if (j > hi) {
          buffer[lo + k] = newList[i];
          i++;
        } else if (compareFunc(newList[i], newList[j]) <= 0) {
          //newList[i] sits before newList[j] ==>  compareFunc(newList[i],newList[j]) < 0
          buffer[lo + k] = newList[i];
          i++;
        } else {
          buffer[lo + k] = newList[j];
          j++;
        }
        k++;
      }
      return buffer;
    }
  },
  mounted() {
    this.$store
      .dispatch("refreshAll")
      .then(() =>
        this.$store.dispatch("getPostById", this.$route.params.postId)
      )
      .then(res => {
        this.post = res;
        this.$store.commit("API_READY");
      });
  },
  components: {
    msgBox,
    BidCard,
    CreateCard,
    parmCard
  },
  $_veeValidate: {
    validator: "new"
  }
};
</script>
