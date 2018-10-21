<template>
  <v-container grid-list-xl >
    <div v-if="api_state != 'READY'" class="text-xs-center">
      <v-progress-circular indeterminate color="primary" />
    </div>
    <v-form ref="form" @submit.prevent="submit" v-else>
      <v-layout wrap>
        <v-flex xs12 sm6>
          <v-text-field v-model="form.title" label="Title *" required></v-text-field>
        </v-flex>
        <addr @confirmLocation="
            loc => {
              // assign the confirmed location to 
              // this property 
              form.location = loc;
            }
          " :address="form.location.address"  hint="Where this event be held?"/>

        <v-flex xs12>
          <dateTime v-model="form.eventTime" title="Event"/>
        </v-flex>
        <v-flex xs12>
          <dateTime v-model="form.bidClosingTime" title="Bid Clossing"/>
        </v-flex>
        <v-flex xs1 ma-0 pa-0>
          <v-btn color="success" type="submit">Submit</v-btn>
        </v-flex>
      </v-layout>
    </v-form>
  </v-container>
</template>

<script>
import addr from "@/components/helper/addressInput.vue";
import dateTime from "@/components/helper/dataTimePicker";

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
      snackText: "Error You must complete all fields with *"
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
          eventTime: this.eventTime,
          bidClosingTime: this.bidClosingTime
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
            // TODO: just a way to implement the snack bar
            this.snackbar = true;
            this.snackbarColor = "error";
            // TODO improve err looking.
            this.snackText = "Error: " + JSON.stringify(err.response.data);
          });
      }
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
    }
  },
  components: {
    addr,
    dateTime
  }
};
</script>
