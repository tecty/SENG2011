<template>
  <v-container>
    <div v-if="api_state != 'WAIT'">
      <!-- content of the post  -->
      <h3 class="display-1 primary--text">
        <span class="grey--text">#{{ post.id }}</span> {{post.title}}
      </h3>

      
    </div>
    <div class="text-xs-center" v-else>
        <v-progress-circular indeterminate color="primary" />
    </div>

    
  </v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex';
export default{
  data(){
    return {
      post:{}
    }
  },
  computed: mapState(['api_state']),
  mounted() {
    this.$store.dispatch('refreshAll').then(()=>
      this.$store.dispatch('getPostById', this.$route.params.postId)
    ).then(res=> {
      this.post = res;
      console.log(this.post);
    });
  }
}
</script>