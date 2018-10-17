<template>
  <v-container grid-list-xl fluid>
    <v-form ref="form" @submit.prevent="submit">
        <v-layout wrap>
          <v-flex xs11 sm5>
            <v-text-field v-model="form.title" 
              label="Title *" required />
          </v-flex>
          <v-flex xs11 sm5>
            <v-select
              v-model="form.event"
              :items="events"
              :rules="[v => !!v || 'Event is required']"
              label="Event"
              item-value="value.title"
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
          <v-flex xs11 sm5>
            <v-text-field v-model="form.peopleCount" 
              label="Number of people *" required />
          </v-flex>
          <v-flex xs11 sm5>
            <v-text-field v-model="form.budget" label="Budget *" required></v-text-field>
          </v-flex>
          <v-flex xs11 sm5>
            <v-text-field v-model="form.title" 
              label="Extra Requirement *" required />
          </v-flex>
        </v-layout>

        <v-btn color="primary" type="submit">Post</v-btn>
        <!-- <v-btn @click="resetForm">Clear</v-btn> -->
    </v-form>
  </v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";
import axios from "axios";

export default {
  data() {
    return {
      form: {
        title: "test",
        event:{},
        message: "test",
        budget: 1,
        peopleCount: 1,
        location: {},
      },
      // this might implement later 
      eventList:[],
      snackbar: false,
      snackbarColor: "error",
      snackText: "Error You must complete all fields with *"
    };
  },
  computed:mapState({
      events: (state) => {
        return state.events.filter((el) => 
          el.owner.username == state.username
        )
      }
    })
  ,
  methods: {
    submit() {
      // axios
      //   .post("posts/", {
      //     title: this.form.title,
      //     message: this.form.message,
      //     eventId: form.event.id, //testing use
      //     location: this.form.location,
      //     budget: this.form.budget,
      //     peopleCount: this.form.peopleCount,
      //     eventTime: this.form.date + "T" + this.form.time,
      //     bidClosingTime: this.form.date10 + "T" + this.form.time11,
      //     extraParameter: [] // TODO extraparameter
      //   })
      console.log(this.events.title);
    }
  },
  mounted() {
    this.$store.dispatch("refreshEvents");
  },
};
</script>
