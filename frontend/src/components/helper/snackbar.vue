<template>
  <v-snackbar v-model="snackbar" absolute top right auto-height :color="snackbarColor">
    <span>{{ snackText }}</span>
    <v-btn dark flat @click="snackbar = false">
      <v-icon dark>check_circle</v-icon>
    </v-btn>
  </v-snackbar>
</template>
