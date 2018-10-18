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
      <v-btn color="success" type="submit">Submit</v-btn>
    </v-form>
</v-container>
</template>

<script>
// TODO: remove axios 
import axios from "axios";
import addr from "@/components/helper/addressInput.vue";
export default {
  data() {
    return {
      form: {
        title: "test",
        message: "test",
        location: {},
        date: "2018-11-13",
        menu: false,
        time: "03:30",
        menu2: false,
        date10: "2018-11-12",
        menu10: false,
        time11: "03:30",
        menu11: false
      },
      // TODO: may be antoher model 
      snackbar: false,
      snackbarColor: "error",
      snackText: "Error You must complete all fields with *"
    };
  },
  methods: {
    submit() {
      axios
        .post("events/", {
          title: this.form.title,
          message: this.form.message,
          eventId: 1, //testing use
          location: this.form.location,
          eventTime: this.form.date + "T" + this.form.time,
          bidClosingTime: this.form.date10 + "T" + this.form.time11
        })
        // TODO: just a way to implement the snack bar
        //        This will be moved to the main frame of the website
        // .then(response => {
        //   // JSON responses are automatically parsed.
        //   this.snackbar = true;
        //   this.snackbarColor = "success";
        //   this.snackText = "Event has been successfully created";
        //   this.events = response.data;
        // })
        .catch(error => {
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            this.snackbar = true;
            this.snackbarColor = "error";
            this.snackText = "Error: " + JSON.stringify(error.response.data); // TODO improve error looking.
          }
        });
      // this.resetForm()
    }
  },
  components: {
    addr
  }
};
</script>
