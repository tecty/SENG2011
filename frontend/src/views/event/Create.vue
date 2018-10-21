<template>
  <v-container grid-list-xl >
    <v-form ref="form" @submit.prevent="submit">
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
          " hint="Where this event be held?"/>
        <v-flex xs12>
          <v-textarea v-model="form.message" color="teal">
            <div slot="label">
              Description
            </div>
          </v-textarea>
        </v-flex>
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

import { mapActions } from "vuex";
export default {
  data() {
    return {
      form: {
        title: "",
        message: "",
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
  methods: {
    ...mapActions(["createEvent"]),
    submit() {
      this.createEvent({
        title: this.form.title,
        message: this.form.message,
        eventId: 1, //testing use
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
  },
  components: {
    addr,
    dateTime
  }
};
</script>
