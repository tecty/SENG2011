<template>
  <v-container grid-list-xl >
    <div v-if="api_state != 'READY' && api_state != 'ERROR'" class="text-xs-center">
      <v-progress-circular indeterminate color="primary" />
    </div>
    <v-form v-else ref="form" @submit.prevent="submit">
        <v-layout row wrap>
          <v-flex xs12 sm6>
            <v-text-field v-model="form.title" 
              label="Title *" required autofocus/>
          </v-flex>
          <v-flex xs12 sm6 v-if="!isEdit">
            <v-select
              v-model="form.event"
              :items="events"
              :rules="[v => !!v || 'Event is required']"
              label="Event"
              required
            ></v-select>
          </v-flex>
        </v-layout>
        <v-layout row wrap>
          <v-flex xs12 v-if="!isEdit">
            <v-textarea v-model="form.message" color="teal">
              <div slot="label">
                Description
              </div>
            </v-textarea>
          </v-flex>
          <v-flex xs12 sm6>
            <v-text-field v-model="form.peopleCount" 
              label="Number of people *" required />
          </v-flex>
          <v-flex xs12 sm6>
            <v-text-field v-model="form.budget" label="Budget *" required></v-text-field>
          </v-flex>
        </v-layout>
        <v-layout row wrap>
          <v-flex xs12>
            <!-- the selection box of extraparams -->
            <extraParamSelector v-model="form.extraParameter"/>
          </v-flex>
          <v-flex xs12 sm6 v-for="(item, index) in error" :key="index">
            {{index}} {{item}}
          </v-flex>
          <v-btn pa-0 color="primary" type="submit">Post</v-btn>
        </v-layout>
        <!-- <v-btn @click="resetForm">Clear</v-btn> -->
    </v-form>
  </v-container>
</template>

<script>
import extraParamSelector from "@/components/extraParam/main.vue";
import { mapState } from "vuex";
export default {
  data() {
    return {
      form: {
        title: "",
        event: "",
        message: "",
        budget: "",
        peopleCount: "",
        location: {},
        extraParam: []
      },
      // this might implement later
      snackbar: false,
      snackbarColor: "error",
      snackText: "Error You must complete all fields with *",
      error: []
    };
  },
  computed: {
    ...mapState({
      events: state => {
        // map the event as an array of name and id
        // in this way, the vuetify selector will show
        // properly
        return state.events
          .filter(
            el =>
              // the event owner must be the logined user
              el.owner.username == state.username &&
              // The event must be valid to create another post
              Date.parse(el.bidClosingTime) > Date.now()
          )
          .map(el => {
            let ret = {};
            ret.text = el.title;
            ret.value = el.id;
            return ret;
          });
      },
      api_state: "api_state"
    }),
    isEdit() {
      // check whether it is edit state
      return this.$route.name == "PostEdit";
    }
  },
  methods: {
    submit() {
      let data = {
        title: this.form.title,
        message: this.form.message,
        budget: this.form.budget,
        peopleCount: this.form.peopleCount,
        extraParameter: this.form.extraParameter,
        event: this.form.event
      };

      // to store the promise object from vuex
      let promise;
      if (!this.isEdit) {
        // only the create mode can have capability to change event
        // perform the create event action
        promise = this.$store.dispatch("createPost", data);
      } else {
        // edit mode will require an id of the post
        data.id = this.form.id;
        // perfrom the edit action by vuex
        promise = this.$store.dispatch("editPost", data);
      }
      promise
        .then(res => {
          this.$router.push({
            name: "PostDetail",
            params: {
              postId: res.data.id
            }
          });
          return res;
        })
        .catch(err => (this.error = err));
    }
  },
  mounted() {
    this.$store.dispatch("requireExtraParams");
    this.$store.dispatch("refreshEvents");
    if (this.isEdit) {
      this.$store.dispatch("getPostById", this.$route.params.postId).then(r => {
        this.form = r.data;
        this.$store.commit("API_READY");
      });
    } else {
      this.$store.commit("API_READY");
    }
  },
  components: {
    extraParamSelector
  }
};
</script>
