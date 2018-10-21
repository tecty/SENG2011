<template>
  <v-layout mb-1>
    <v-flex>
      <v-card color="" class="">
        <div>
          <div class="pl-3 pa-2">
            <span class="primary--text font-weight-bold">{{ msg.owner.username }}:</span>
            {{ msg.msg }}
            <v-form v-if="isReply"  @submit.prevent="submit" lazy-validation>
              <v-text-field v-model="replyMsg" label="Message" required />
              <v-btn class="ma-0" flat color="primary" @click="submit">Reply</v-btn>
            </v-form>
            <div v-else>
              <v-btn class="ma-0" flat color="primary" @click="()=>{isReply=true}" >
                Reply
              </v-btn>
            </div>
          </div>
          <!-- these two reply button has different meaning -->
        </div>
        <div v-for="msg in msg.sub_msg" :key="msg.id">
          <msgBox class="ml-1" :msg="msg" @requireRefresh="()=> {
            $emit('requireRefresh')
          }"/>
        </div>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "msgBox",
  props: ["msg"],
  data() {
    return {
      // indicate the return box is expanded
      isReply: false,
      replyMsg: ""
    };
  },
  methods: {
    ...mapActions(["createMsg"]),
    submit() {
      this.createMsg({
        parentMsg: this.msg.id,
        msg: this.replyMsg
      }).then(()=> {
        console.log("emit at submit");
        this.$emit("requireRefresh")
      });
    }
  }
};
</script>
