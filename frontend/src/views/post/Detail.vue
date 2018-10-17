<template>
  <v-container>
    <div v-if="api_state == 'READY'">
      <!-- content of the post  -->
      <h3 class="display-1 primary--text">
        <span class="grey--text">#{{ post.id }}</span> {{post.title}}
      </h3>
      <p>{{ post.state | stateToText}}</p>
      <h5 class="headline primary--text ">Issuer:</h5>
      {{ post.event.owner.username }}
      <h5 class="headline primary--text ">Event Time:</h5>
      {{ post.event.eventTime }}
      <h5 class="headline primary--text ">Bid End:</h5>
      {{ post.event.bidClosingTime }}
      <h5 class="headline primary--text ">
        peopleCount
      </h5>{{post.peopleCount}} 
      <h5 class="headline primary--text ">
        Budget
      </h5>${{post.budget}} 
      <parmCard :criteria="post.extraParameter"></parmCard>
    </div>
    <div class="text-xs-center" v-else>
      <v-progress-circular indeterminate color="primary" />
    </div>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
import parmCard from "@/components/post/extraParm.vue";
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
    parmCard
  }
};
</script>
