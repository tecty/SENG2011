<template>
  <v-layout row wrap>
    <v-flex xs12 sm6 md4 pt-0>
     <v-menu
        ref="dateMenu"
        :close-on-content-click="false"
        v-model="dateMenu"
        :nudge-right="40"
        :return-value.sync="date"
        lazy
        transition="scale-transition"
        offset-y
        full-width
        min-width="290px"
      >
        <v-text-field
          slot="activator"
          v-model="date"
          :label="getDateTitle"
          prepend-icon="event"
          readonly
        ></v-text-field>
        <v-date-picker v-model="date" 
          @input="dateChanged"
          :allowed-dates="allowDates" 
          landscape />
      </v-menu>
    </v-flex>
    <v-flex xs12 sm6 md4 pt-0>
      <v-menu ref="timeMenu" :close-on-content-click="false" v-model="timeMenu" :nudge-right="40" :return-value.sync="time"
        lazy transition="scale-transition" offset-y full-width max-width="290px" min-width="290px">
        <v-text-field slot="activator" v-model="time" :label="getTimeTitle"
         prepend-icon="access_time" readonly required></v-text-field>
        <v-time-picker v-if="timeMenu" v-model="time" @change="timeChanged" format="24hr"></v-time-picker>
      </v-menu>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: ["title", "value"],
  data() {
    return {
      dateMenu: null,
      date: null,
      timeMenu: null,
      time: null
    };
  },
  computed: {
    getTitle() {
      // undefined guard of the title property
      if (this.title != undefined) {
        return this.title;
      }
      return "";
    },
    getDateTitle() {
      return `${this.getTitle} Date*`;
    },
    getTimeTitle() {
      return `${this.getTitle} Time*`;
    }
  },
  methods: {
    allowDates(val) {
      let d1 = new Date();
      let d2 = new Date(val);
      d2.setDate(d2.getDate() + 1);
      return d2 >= d1;
    },
    emitEvent() {
      if (this.date && this.time) {
        // there are inputed date and time
        this.$emit("input", `${this.date}T${this.time}`);
      }
    },
    timeChanged() {
      // save the picked time
      this.$refs.timeMenu.save(this.time);
      // set the menu to be not shown
      this.timeMenu = false;
      this.emitEvent();
    },
    dateChanged() {
      // save the picked date
      this.$refs.dateMenu.save(this.date);
      // set the date menu to be hidden
      this.dateMenu = false;
      this.emitEvent();
    }
  },
  mounted() {
    // TODO: check the binded whether the bind value is given, if
    // it's, assign the value to time and date
    if (this.value && this.value !== "") {
      let arr = this.value.split("T");
      this.date = arr[0];
      this.time = arr[1].substring(0, 5);
    }
  }
};
</script>

<style>
</style>
