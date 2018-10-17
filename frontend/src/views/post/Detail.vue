<template>
  <v-container>
<<<<<<< HEAD
    <div v-if="api_state != 'WAIT'">
=======
    <div v-if="api_state == 'READY'">
>>>>>>> tecty/it5
      <!-- content of the post  -->
      <h3 class="display-1 primary--text">
        <span class="grey--text">#{{ post.id }}</span> {{post.title}}
      </h3>
      <p>{{ post.state | stateToText}}</p>
<<<<<<< HEAD
=======
      <h5 class="headline primary--text ">Issuer:</h5>
      {{ post.event.owner.username }}
      <h5 class="headline primary--text ">Event Time:</h5>
      {{ post.event.eventTime }}
      <h5 class="headline primary--text ">Bid End:</h5>
      {{ post.event.bidClosingTime }}
>>>>>>> tecty/it5
      <h5 class="headline primary--text ">
        peopleCount
      </h5>{{post.peopleCount}} 
      <h5 class="headline primary--text ">
        Budget
      </h5>${{post.budget}} 
<<<<<<< HEAD
      <h5 class="headline primary--text ">
        Criterias
      </h5>{{post.extraParameter}}
    </div>
    
    <div class="text-xs-center" v-else>
        <v-progress-circular indeterminate color="primary" />
    </div>

    
=======
      <parmCard :criteria="post.extraParameter"></parmCard>
    </div>
    <div class="text-xs-center" v-else>
      <v-progress-circular indeterminate color="primary" />
    </div>
>>>>>>> tecty/it5
  </v-container>
</template>

<script>
<<<<<<< HEAD
import { mapActions, mapState } from "vuex";
=======
import { mapState } from "vuex";
import parmCard from "@/components/post/extraParm.vue";
>>>>>>> tecty/it5
export default {
  data() {
    return {
      post: {}
    };
  },
  computed: mapState(["api_state"]),
  mounted() {
<<<<<<< HEAD
    this.$store.dispatch("requireExtraParams");
=======
>>>>>>> tecty/it5
    this.$store
      .dispatch("refreshAll")
      .then(() =>
        this.$store.dispatch("getPostById", this.$route.params.postId)
      )
      .then(res => {
        this.post = res;
<<<<<<< HEAD
        console.log(this.post);
      });
  },
  validKey(key) {
    return true;
=======
        this.$store.commit("API_READY");
      });
  },
  components: {
    parmCard
>>>>>>> tecty/it5
  }
};
</script>
