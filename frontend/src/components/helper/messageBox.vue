<template>
  <v-layout>
    <v-flex>
      <v-card color="blue-grey" class="white--text">
        <v-card-title primary-title>
          <div>
            <h3 class="headline mb-0">Unlimited music now</h3>
            Listen to your favorite artists and albums whenever and wherever, online and offline.
          </div>
        </v-card-title>
        <v-card-actions>
          <v-btn flat dark>Reply</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
   
  </v-layout>
</template>

<script>
export default {
  props: ["msg"],
  data() {
    return {};
  },
};
</script>
