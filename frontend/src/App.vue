<template>
  <v-app>
    <app-toolbar />
    <v-content>
      <router-view/>
    </v-content>
    <v-footer app>
      <span>SENG2011 PartyWhip &copy; 2018</span>
    </v-footer>
  </v-app>  
</template>


<script>
import AppToolbar from "./components/AppToolbar.vue";
export default {
  name: "App",
  components: { AppToolbar },
  filters: {
    stateToText: function (s) {
      switch (s) {
        case 'BD': return 'Bidding';break;
        case 'DL': return 'Deal'; break;
        case 'FN': return 'Finished'; break;
        case 'CL': return 'Canceled'; break;
        case 'SD': return 'Selected'; break;
        case 'US': return 'Unselected'; break;
        default:
          return 'Unknown'+ s;
          break;
      }
    }
  }
};
</script>

<style>
a {
  color: black;
  /* remove the underline in link */
  text-decoration: none;
}
</style>
