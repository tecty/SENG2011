<template>
  <v-layout row ma-3>
    <v-flex md10 offset-md1 xs12 offset-xs0 lg6 offset-lg3>
      <h1>Sign Up</h1>
      <v-form v-model="valid" @submit.prevent="register">
        <v-text-field
          v-model="username" label="Username" required autofocus 
          autocomplete
        />
        <v-text-field 
          v-model="password" :type="show? 'text':'password'" label="Password" 
          :append-icon= "show ? 'visibility' : 'visibility_off'"
          autocomplete @click:append="show = !show" 
          required 
        />
        <v-text-field 
          v-model="passwordAgain" :type="show? 'text':'password'" label="Password Again" 
          :append-icon= "show ? 'visibility' : 'visibility_off'"
          autocomplete @click:append="show = !show" 
          required 
        />
        <v-text-field 
          v-model="tel" type="text" label="Telephone" 
          autocomplete 
          required 
        />
        <addr 
          @confirmLocation="
            loc => {
              // assign the confirmed location to 
              // this property 
              location = loc;
            }
          "
        ></addr>
        <p></p>
        <p>{{error}}</p>
        <v-btn type="submit" >Login</v-btn>
      </v-form>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapActions } from "vuex";
// import postCard from "@/components/helper/addressInput";
import addr from "@/components/helper/addressInput.vue";
export default {
  data() {
    return {
      // prevent error because vuetify require this
      valid: false,
      // input of username and password
      username: "",
      password: "",
      passwordAgain: "",
      location: {},
      // if show == true, show the password
      show: false,
      tel: "",
      error: ""
    };
  },
  methods: {
    // map the login action from vuex
    ...mapActions(["registerByUser"]),
    register() {
      this.registerByUser({
        username: this.username,
        password: this.password,
        password_again: this.passwordAgain,
        location: this.location,
        tel: this.tel
      })
        .then(() => {
          // go to main page
          if (this.$route.query.redirect) {
            // redirect request from another view
            this.$router.push(this.$route.query.redirect);
          } else {
            // go to previous page, if it's user direct to login
            this.$router.go(-2);
          }
        })
        .catch(err => {
          console.log(err);
          this.error = err.response.data;
        });
    }
  },
  components: {
    addr
  }
};
</script>