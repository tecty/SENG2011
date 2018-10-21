<template>
  <v-container grid-list-xl >
    <v-form ref="form" @submit.prevent="submit">
        <v-layout wrap>
          <v-flex xs12 sm6>
            <v-text-field v-model="form.title" 
              label="Title *" required autofocus/>
          </v-flex>
          <v-flex xs12 sm6>
            <v-select
              v-model="form.event"
              :items="events"
              :rules="[v => !!v || 'Event is required']"
              label="Event"
              required
            ></v-select>
          </v-flex>
          <v-flex xs12>
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
          <v-flex xs12>
            <!-- the selection box of extraparams -->
            {{form.extraParam}}
            <extraParamSelector v-model="form.extraParam"/>
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
import extraParamSelector from '@/components/extraParam/main.vue'
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
  computed: mapState({
    events: state => {
      return state.events
        .filter(el => el.owner.username == state.username)
        .map(el => {
          let ret = {};
          ret.text = el.title;
          ret.value = el.id;
          return ret;
        });
    }
  }),
  methods: {
    submit() {
      let data = {
        title: this.form.title,
        message: this.form.message,
        event: this.form.event,
        budget: this.form.budget,
        peopleCount: this.form.peopleCount,
        extraParameter: [] // TODO extraparameter
      };
      this.$store
        .dispatch("createPost", data)
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
  },
  components: {
    extraParamSelector
  }

};
</script>
