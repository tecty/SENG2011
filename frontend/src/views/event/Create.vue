<template>
  <v-container grid-list-xl >
    <div v-if="api_state != 'READY' && api_state != 'ERROR'" class="text-xs-center">
      <v-progress-circular indeterminate color="primary" />
    </div>

    <form ref="form" @submit.prevent="submit" v-else>
          <v-snackbar
      v-model="snackbar"
    >
      {{snackText}}
      <v-btn flat color="error" @click.native="snackbar = false">Close</v-btn>
    </v-snackbar>
      <v-layout wrap>
        <v-flex xs12 sm6>
          <v-text-field v-model="form.title"
          v-validate="'required'" data-vv-name="title"  :error-messages="errors.collect('title')"
           label="Title *"></v-text-field>
        </v-flex>
        <addr @confirmLocation="
            loc => {
              // assign the confirmed location to 
              // this property 
              form.location = loc;
            }
          " :address="form.location.address"  hint="Where this event be held?"/>

        <v-flex xs12>
          <dateTime v-model="form.eventTime" 
          title="Event"/>
        </v-flex>
        <v-flex xs12>
          <dateTime v-model="form.bidClosingTime" title="Bid Clossing"/>
        </v-flex>
        <v-flex xs1 ma-0 pa-0>
          <v-btn color="success" type="submit">Submit</v-btn>
        </v-flex>
      </v-layout>
    </form>
  </v-container>
</template>

<script>
import addr from "@/components/helper/addressInput.vue";
import dateTime from "@/components/helper/dataTimePicker";
import snackBar from "@/components/helper/snackbar";

import { mapActions, mapState } from "vuex";
export default {
  data() {
    return {
      form: {
        title: "",
        location: {},
        eventTime: null,
        bidClosingTime: null
      },
      // TODO: may be antoher model
      snackbar: false,
      snackbarColor: "error",
      snackText:
        "Error: You must complete all fields with * and choose correct time and address"
    };
  },
  computed: {
    ...mapState(["api_state"]),
    isEdit() {
      return this.$route.name == "EventEdit";
    }
  },
  methods: {
    ...mapActions(["createEvent", "editEvent"]),
    submit() {
      this.$validator.validateAll().then(result => {
        if (result) {
          if (this.isEdit) {
            this.editEvent(this.form).then(ret => {
              this.$router.push({
                name: "EventDetail",
                params: {
                  eventId: ret.data.id
                }
              });
            });
          } else {
            // create the event
            this.createEvent({
              title: this.form.title,
              location: this.form.location,
              eventTime: this.form.eventTime,
              bidClosingTime: this.form.bidClosingTime
            })
              .then(res => {
                let eventId = res.data.id;
                this.$router.push({
                  name: "EventDetail",
                  params: {
                    eventId: eventId
                  }
                });
              })
              .catch(err => {
                if (!this.form.location) {
                  this.snackText = "please select a correct address";
                } else if (!this.form.eventTime || !this.form.bidClosingTime) {
                  this.snackText = "please input correct time and date";
                } else {
                  let d1 = Date.parse(this.form.eventTime);
                  let d2 = Date.parse(this.form.bidClosingTime);
                  if (d2 > d1) {
                    this.snackText =
                      "bids must close later than now, and event should start after bid close ";
                  }
                }
                this.snackbar = true;
                this.snackbarColor = "error";
                this.$store.commit("API_READY");
              });
          }
        }
      });
    }
  },
  mounted() {
    // assign the detail from vuex
    if (this.isEdit) {
      // handy event id fetch from route
      let eventId = this.$route.params.eventId;
      this.$store.dispatch("getEventById", eventId).then(res => {
        this.form = res.data;
        this.$store.commit("API_READY");
      });
    } else {
      this.$store.commit("API_READY");
    }
  },
  components: {
    addr,
    dateTime
  }
};
</script>
