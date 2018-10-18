<template>
  <v-container>
    <v-layout row wrap>
        <v-flex xs12>
          <v-card color="blue-grey darken-2" class="white--text">
            <v-card-title primary-title>
              <div class="headline">Unlimited music now</div>
              <div>Listen to your favorite artists and albums whenever and wherever, online and offline.</div>
            </v-card-title>
            <v-card-actions>
              <v-btn flat dark>Reply</v-btn>
            </v-card-actions>
            <messageBox />
          </v-card>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import messageBox from "./messageBox.vue";
export default {
  props: ["msg"],
  data() {
    return {};
  },
  components: {
    messageBox
  }
};
</script>
