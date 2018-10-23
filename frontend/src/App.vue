<template>
  <v-app>
    <!-- nav drawer -->
    <v-navigation-drawer v-model="drawer" absolute temporary class="grey lighten-4">
      <v-list class="grey lighten-4">
        <template v-for="(item, i) in items">
          <v-layout v-if="item.heading" :key="i" row align-center>
            <v-flex xs6>
              <v-subheader v-if="item.heading">
                {{ item.heading }}
              </v-subheader>
            </v-flex>
            <v-flex xs6 class="text-xs-right">
              <v-btn small flat>edit</v-btn>
            </v-flex>
          </v-layout>
          <v-divider v-else-if="item.divider" :key="i" dark class="my-3"></v-divider>
          <v-list-tile :to="item.href" v-else :key="i">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title >
                {{ item.text }}
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-navigation-drawer>
    <!-- nav toolbar -->
    <v-toolbar app :clipped-left="clipped">
      <v-toolbar-side-icon @click.stop="drawer = !drawer" />
      <router-link to="/">
        <v-toolbar-title class="black--text">PartyWhip</v-toolbar-title>
      </router-link>
      <v-spacer />
      <v-btn v-if="!username" to="login" flat>Login</v-btn>
      <v-btn v-else @click="logout" flat>Logout</v-btn>
    </v-toolbar>
    <!-- main content -->
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      drawer: null,
      clipped: null,
      items: [
        {
          icon: "home",
          text: "Home",
          href: "/"
        },
        { divider: true },
        {
          icon: "group",
          text: "Event",
          href: "/event"
        },
        {
          icon: "restaurant",
          text: "Post",
          href: "/post"
        }
      ]
    };
  },
  computed: {
    ...mapState(["username"])
  },
  methods: {
    ...mapActions({
      logoutInVuex: "logout"
    }),
    logout() {
      this.logoutInVuex();
      this.$router.push("/");
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
