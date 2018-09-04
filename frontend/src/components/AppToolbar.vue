<template>
  <div>
    <v-navigation-drawer 
      persistent :mini-variant="miniVariant" :clipped="clipped" v-model="drawer"
      enable-resize-watcher fixed app
    >
      <v-list>
        <!-- https://stackoverflow.com/questions/47586022/router-link-with-vue-and-vuetify-confusion -->
        <v-list-tile value="true" v-for="(item, i) in items" :key="i" 
          :to="item.href"
        >
          <v-list-tile-action>
            <v-icon v-html="item.icon"></v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title v-text="item.title"></v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app :clipped-left="clipped">
      <v-toolbar-side-icon @click.stop="drawer = !drawer" />
      <v-btn icon @click.stop="miniVariant = !miniVariant">
        <v-icon v-html="miniVariant ? 'chevron_right' : 'chevron_left'" />
      </v-btn>
      <v-btn icon @click.stop="clipped = !clipped">
        <v-icon>web</v-icon>
      </v-btn>
      <v-btn icon @click.stop="fixed = !fixed">
        <v-icon>remove</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer />
      <v-btn v-if="!token" to="login"  flat>Login</v-btn>
      <v-btn v-else @click="logoutWrapper" flat>Logout</v-btn>
    </v-toolbar>
  </div>

</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  data() {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      items: [
        {
          icon: "bubble_chart",
          title: "Inspire",
          href: "/"
        },
        {
          icon: "home",
          title: "Home",
          href: "/"
        },
        {
          icon: "restaurant",
          title: "Post",
          href: "post"
        }
      ],
      miniVariant: true,
      right: true,
      rightDrawer: false,
      title: "PartyWhip"
    };
  },
  methods: {
    ...mapActions(["logout"]),
    logoutWrapper() {
      this.logout();
      this.$router.push("/");
    }
  },
  computed: {
    // this just check wether the user has logined
    ...mapState(["token"])
  }
};
</script>
