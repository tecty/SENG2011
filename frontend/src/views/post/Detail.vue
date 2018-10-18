<template>
  <v-container full-height>
    <div v-if="api_state == 'READY'">
      <!-- content of the post  -->
      <h3 class="display-1 primary--text">
        <span class="grey--text">#{{ post.id }}</span> {{post.title}}
      </h3>
      <p>{{ post.state | stateToText}}</p>
      <h5 class="headline primary--text ">Issuer:</h5>
      <p>{{ post.event.owner.username }}</p>
      <h5 class="headline primary--text ">Event Time:</h5>
      <p>{{ post.event.eventTime }}</p>
      <h5 class="headline primary--text ">Bid End:</h5>
      <p>{{ post.event.bidClosingTime }}</p>
      <h5 class="headline primary--text ">
        peopleCount
      </h5>
      <p>{{post.peopleCount}} </p>
      <h5 class="headline primary--text ">
        Budget
      </h5>
      <p>${{post.budget}}</p>
      <parmCard :criteria="post.extraParameter" />
      <msgBox></msgBox>
    </div>
    <div class="text-xs-center" v-else>
      <v-progress-circular indeterminate color="primary" />
    </div>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import parmCard from "@/components/post/extraParm.vue";
import msgBox from "@/components/helper/messageBox.vue";
export default {
  data() {
    return {
      post: {}
    };
  },
  computed: mapState(["api_state"]),
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
    parmCard,
    msgBox
  }
};
</script>
