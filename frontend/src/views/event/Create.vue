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
          <v-layout row wrap>
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
            <v-flex xs12 sm6 md4>
              <v-menu ref="menu2" :close-on-content-click="false" v-model="form.menu2" :nudge-right="40" :return-value.sync="form.time"
                lazy transition="scale-transition" offset-y full-width max-width="290px" min-width="290px">
                <v-text-field slot="activator" v-model="form.time" label="Event Time *" prepend-icon="access_time" readonly required></v-text-field>
                <v-time-picker v-if="form.menu2" v-model="form.time" @change="$refs.menu2.save(form.time)"></v-time-picker>
              </v-menu>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs12>
          <v-layout row wrap>
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
            <v-flex xs12 sm6 md4>
              <v-menu ref="menu11" :close-on-content-click="false" v-model="form.menu11" :nudge-right="40" :return-value.sync="form.time11"
                lazy transition="scale-transition" offset-y full-width max-width="290px" min-width="290px">
                <v-text-field slot="activator" v-model="form.time11" label="Bid Closing Time *" prepend-icon="access_time" readonly required></v-text-field>
                <v-time-picker v-if="form.menu11" v-model="form.time11" @change="$refs.menu11.save(form.time11)"></v-time-picker>
              </v-menu>
            </v-flex>
          </v-layout>
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
import { mapActions } from "vuex";
export default {
  data() {
    return {
      form: {
        title: "",
        message: "",
        location: {},
        date: "",
        menu: false,
        time: null,
        menu2: false,
        date10: "",
        menu10: false,
        time11: null,
        menu11: false
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
        eventTime: this.form.date + "T" + this.form.time,
        bidClosingTime: this.form.date10 + "T" + this.form.time11
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
    addr
  }
};
</script>
