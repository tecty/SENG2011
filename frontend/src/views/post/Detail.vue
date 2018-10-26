<template>
  <v-container full-height>
    <div v-if="api_state != 'READY' && api_state != 'ERROR'" class="text-xs-center">
      <v-progress-circular indeterminate color="primary" />
    </div>
    <div v-else>
      <!-- content of the post  -->
      <v-layout row wrap>
        <h3 class="display-1 primary--text">
          <span class="grey--text">#{{ post.id }}</span> {{post.title}}
        </h3>
        <v-spacer></v-spacer>
        <div v-if="canEdit">
          <v-btn color="error" @click="cancel">Cancel</v-btn>
          <v-btn color="primary" :to="{
            name:'PostEdit',
            params: {
              postId:post.id,
            }
          }">Edit</v-btn>

        </div>
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
      <h5 class="headline primary--text ">Event Address:</h5>
      <p>{{ post.event.location.address }}</p>
      <h5 class="headline primary--text ">
        Message
      </h5>
      <msgBox :msg="post.msg" class="mb-3"/>
      <v-layout>
        <v-flex xs12>
          <h5 class="headline primary--text ">
            Bid
          </h5>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-flex xs12 sm8 md6 lg3>
          <sortingSelector :sortBy="sortParameter" v-model="post.bid_set" />
        </v-flex>
      </v-layout>
      <v-layout row wrap>
          <!-- select sorting parameter  -->
          <!-- cards of bids -->
          <v-flex xs12 md6 lg4 v-for="bid in post.bid_set" :key="bid.id">
            <bid-card :bid="bid" :post="post" @requireRefresh="()=> refreshContent()" />
          </v-flex>
          <!-- card for bidding -->
        <v-flex xs12 md6 lg4>
          <CreateCard v-if="canBid" :postId="post.id" @requireRefresh="()=> refreshContent()" />
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
        {
          text: "Lastest",
          value: {
            id: 0,
            f: (a, b) => a.id - b.id
          }
        },
        {
          text: "Offer Price",
          value: {
            id: 1,
            f: (a, b) => -(parseInt(a.price, 10) - parseInt(b.price, 10))
          }
        },
        {
          text: "Bidder Name",
          value: {
            id: 2,
            f: (a, b) => a.owner.username.localeCompare(b.owner.username)
          }
        },
        {
          text: "Default",
          value: {
            id: 3,
            f: (a, b) => a.id - b.id
          }
        }
      ]
    };
  },
  computed: {
    ...mapState({
      api_state: "api_state",
      username: state => state.username
    }),
    canBid() {
      return (
        this.api_state == "READY" &&
        this.post.event.owner.username != this.username &&
        this.post.state == "BD"
      );
    },
    canEdit() {
      return (
        this.post.event.owner.username == this.username &&
        this.post.state == "BD"
      );
    },
    isUserSelected(){
      // this is prepare for condition link - 3.4.2
      // the bid of current user 
      let bid = this.post.bid_set.find(b=> b.owner.username == this.username);
      if(bid && bid.state == "SD"){
        // this bidder is selected
        return true;
      }
      return false;
    }
  },
  methods: {
    ...mapActions(["refreshAll", "getPostById", "cancelPostById"]),

    refreshContent() {
      this.refreshAll().then(() => {
        // assign the new post object
        this.post = this.$store.state.posts.find(el => el.id == this.post.id);
        // declear the page is re-rendered
        this.$store.commit("API_READY");
      });
    },
    cancel(){
      this.cancelPostById(this.post.id).then(()=> this.$router.push('/'));
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
