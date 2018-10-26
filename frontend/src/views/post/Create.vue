<template>
  <v-container grid-list-xl>
    <div v-if="api_state != 'READY' && api_state != 'ERROR'" class="text-xs-center">
      <v-progress-circular indeterminate color="primary" />
    </div>
    <form v-else ref="form" @submit.prevent="submit">
      <v-layout row wrap>
        <v-flex xs12 sm6>
          <v-text-field v-model="form.title" v-validate="'required'" data-vv-name="title" :error-messages="errors.collect('title')"
            label="Title *" autofocus/>
        </v-flex>
        <v-flex xs12 sm6 v-if="!isEdit">
          <v-select v-model="form.event" :items="events" v-validate="'required'" data-vv-name="event" :error-messages="errors.collect('event')"
            label="Event"></v-select>
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
          <v-text-field v-model="form.peopleCount" v-validate="'required|min_value:1'" data-vv-name="number of people" :error-messages="errors.collect('number of people')"
            label="Number of people *" />
        </v-flex>
        <v-flex xs12 sm6>
          <v-text-field v-model="form.budget" v-validate="'required|min_value:1'" data-vv-name="budegt" :error-messages="errors.collect('budegt')"
            label="Budget *"></v-text-field>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-flex xs12>
          <!-- the selection box of extraparams -->
          <extraParamSelector v-model="form.extraParameter" />
        </v-flex>
        <v-flex xs12 sm6 v-for="(item, index) in error" :key="index">
          {{index}} {{item}}
        </v-flex>
        <v-btn pa-0 color="primary" type="submit">Post</v-btn>
      </v-layout>
      <!-- <v-btn @click="resetForm">Clear</v-btn> -->
    </form>
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
        extraParam: [],
        //dictionary for vee-vaildator
        dictionary: {
          attributes: {
            email: "E-mail Address"
            // custom attributes
          },
          custom: {
            name: {
              required: () => "Name can not be empty",
              max: "The name field may not be greater than 10 characters"
              // custom messages
            },
            select: {
              required: "Select field is required"
            }
          }
        }
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
          .filter(el => el.owner.username == state.username)
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
      this.$validator.validateAll().then(result => {
        if (result) {
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
            .catch(err => {
              this.error = err;
              this.$store.commit("API_READY");
            });
        }
      });
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