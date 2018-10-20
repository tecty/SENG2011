<template>
  <v-layout mb-1>
    <v-flex>
      <v-card color="" class="">
        <v-card-media primary-title>
          <div class="pl-3 pa-2">
            <span class="primary--text font-weight-bold">{{ msg.owner.username }}:</span>
            {{ msg.msg }}
          </div>
          <!-- these two reply button has different meaning -->
          <form v-if="isReply" >

          </form>
          <v-btn v-else flat color="primary" @click="()=>{isReply=true}" >Reply</v-btn>
        </v-card-media>
        <div v-for="msg in msg.sub_msg" :key="msg.id">
          <msgBox class="ml-1" :msg="msg" />
        </div>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: "msgBox",
  props: ["msg"],
  data() {
    return {
      // indicate the return box is expanded 
      isReply: false,
    };
  },
  methods:{
    ...mapActions(['createMsg']),
    reply(){
      this.createMsg({
        parentMsg: msg.id, 
        msg:this.from.msg
      }).then(this.$emit('refreshRequired'));
    }
  }
};
</script>
