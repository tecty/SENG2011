<template>
  <v-card flat>
    <v-snackbar v-model="snackbar" absolute top right auto-height :color="snackbarColor">
      <span>{{ snackText }}</span>
      <v-btn dark flat @click="snackbar = false">
        <v-icon dark>check_circle</v-icon>
      </v-btn>
    </v-snackbar>
    <v-form ref="form" @submit.prevent="submit">
      <v-container grid-list-xl fluid>
        <v-layout wrap>
          <v-flex xs12 sm6>
            <v-text-field v-model="form.title" label="Title *" required></v-text-field>
          </v-flex>
          <v-flex xs12 sm6>
            <v-text-field v-model="form.location" label="Location *" required></v-text-field>
          </v-flex>
          <v-flex xs12>
            <v-textarea v-model="form.message" color="teal">
              <div slot="label">
                Description
              </div>
            </v-textarea>
          </v-flex>

          <v-flex xs12 sm6 md4>
            <v-menu ref="menu" :close-on-content-click="false" v-model="form.menu" :nudge-right="40" :return-value.sync="form.date" lazy
              transition="scale-transition" offset-y full-width min-width="290px">
              <v-text-field slot="activator" v-model="form.date" label="Event Date *" prepend-icon="event" readonly required></v-text-field>
              <v-date-picker v-model="form.date" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn flat color="primary" @click="$refs.menu.save(form.date)">OK</v-btn>
              </v-date-picker>
            </v-menu>
          </v-flex>
          <v-flex xs11 sm5>
            <v-menu ref="menu2" :close-on-content-click="false" v-model="form.menu2" :nudge-right="40" :return-value.sync="form.time"
              lazy transition="scale-transition" offset-y full-width max-width="290px" min-width="290px">
              <v-text-field slot="activator" v-model="form.time" label="Event Time *" prepend-icon="access_time" readonly required></v-text-field>
              <v-time-picker v-if="form.menu2" v-model="form.time" @change="$refs.menu2.save(form.time)"></v-time-picker>
            </v-menu>
          </v-flex>
          <v-flex xs12 sm6 md4>
            <v-menu ref="menu10" :close-on-content-click="false" v-model="form.menu10" :nudge-right="40" :return-value.sync="form.date10"
              lazy transition="scale-transition" offset-y full-width min-width="290px">
              <v-text-field slot="activator" v-model="form.date10" label="Bid Closing Date *" prepend-icon="event" readonly required></v-text-field>
              <v-date-picker v-model="form.date10" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn flat color="primary" @click="$refs.menu10.save(form.date10)">OK</v-btn>
              </v-date-picker>
            </v-menu>
          </v-flex>
          <v-flex xs11 sm5>
            <v-menu ref="menu11" :close-on-content-click="false" v-model="form.menu11" :nudge-right="40" :return-value.sync="form.time11"
              lazy transition="scale-transition" offset-y full-width max-width="290px" min-width="290px">
              <v-text-field slot="activator" v-model="form.time11" label="Bid Closing Time *" prepend-icon="access_time" readonly required></v-text-field>
              <v-time-picker v-if="form.menu11" v-model="form.time11" @change="$refs.menu11.save(form.time11)"></v-time-picker>
            </v-menu>
          </v-flex>
        </v-layout>
      </v-container>

      <v-card-actions>
        <v-btn color="primary" type="submit">Submit</v-btn>
        <v-btn @click="resetForm">Clear</v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
import axios from "axios";
export default {
  data() {
    const defaultForm = Object.freeze({
      title: "test",
      message: "test",
      location: "test",
      date: "2018-11-13",
      menu: false,
      time: "03:30",
      menu2: false,
      date10: "2018-11-12",
      menu10: false,
      time11: "03:30",
      menu11: false
    });
    return {
      form: Object.assign({}, defaultForm),
      snackbar: false,
      snackbarColor: "error",
      snackText: "Error You must complete all fields with *"
    };
  },
  methods: {
    resetForm() {
      this.form = Object.assign({}, this.defaultForm);
      this.$refs.form.reset();
    },
    submit() {
      axios
        .post("events/", {
          title: this.form.title,
          message: this.form.message,
          eventId: 1, //testing use
          location: this.form.location,
          eventTime: this.form.date + "T" + this.form.time,
          bidClosingTime: this.form.date10 + "T" + this.form.time11,
        })
        .then(response => {
          // JSON responses are automatically parsed.
          console.log(response);
          this.snackbar = true;
          this.snackbarColor = "success";
          this.snackText = "Event has been successfully created";
          this.events = response.data;
          this.resetForm();
        })
        .catch(error => {
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
            this.snackbar = true;
            this.snackbarColor = "error";
            this.snackText = "Error: " + JSON.stringify(error.response.data); // TODO improve error looking.
          } else if (error.request) {
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
            // http.ClientRequest in node.js
            console.log(error.request);
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log("Error", error.message.data);
          }
          console.log(error.config);
        });
      // this.resetForm()
    }
  }
};
</script>