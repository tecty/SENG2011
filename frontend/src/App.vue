<template>
  <v-app>
    <app-toolbar />
    <v-content>
      <router-view/>
    </v-content>

    <v-footer app>
      <span>&copy; 2017</span>
    </v-footer>
  </v-app>
</template>


<script>
import AppToolbar from "./components/AppToolbar.vue";
export default {
  name: "App",
  components: { AppToolbar }
};
</script>

<style>
a {
  color: black;
  /* remove the underline in link */
  text-decoration: none;
}
</style>
