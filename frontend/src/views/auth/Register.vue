<template>
  <v-container grid-list-xs>
    <div v-if="api_state != 'READY' && api_state != 'ERROR'" class="text-xs-center">
      <v-progress-circular indeterminate color="primary" />
    </div>
    <div v-else>
      <v-layout row ma-3>
        <v-flex md10 offset-md1 xs12 offset-xs0 lg6 offset-lg3 >
          <h1 v-if="!isEdit">Sign Up</h1>
          <h1 v-else>Edit Profile</h1>

          <form @submit.prevent="register">
          <v-snackbar v-model="snackbar">
              {{snackText}}
             <v-btn flat color="error" @click.native="snackbar = false">Close</v-btn>
          </v-snackbar>
            <v-text-field
              v-model="username" label="Username" required autofocus 
               v-validate="'required'" data-vv-name="username" :error-messages="errors.collect('username')"
              autocomplete
            />
            <v-text-field 
              v-model="password" :type="show? 'text':'password'" label="Password" 
              :append-icon= "show ? 'visibility' : 'visibility_off'"
               v-validate="'required'" ref="password" data-vv-name="password" :error-messages="errors.collect('password')"
              autocomplete @click:append="show = !show" 
              required 
            />
            <v-text-field 
              v-model="passwordAgain" :type="show? 'text':'password'" label="Password Again" 
               v-validate="'required|confirmed:password'" data-vv-name="password confirm" :error-messages="errors.collect('password confirm')"
              :append-icon= "show ? 'visibility' : 'visibility_off'"
              autocomplete @click:append="show = !show" 
              required 
            />
            <v-text-field 
              v-model="tel" type="text" label="Telephone" 
               v-validate="'required|numeric'" data-vv-name="Telephone" :error-messages="errors.collect('Telephone')"
              autocomplete 
            />
            <addr 
              @confirmLocation="
                loc => {
                  // assign the confirmed location to 
                  // this property 
                  location = loc;
                }
              "
              :address="location.address"
              hint="Where's your address?"
            ></addr>
            <p></p>
            <v-btn type="submit" v-if="!isEdit" >Register</v-btn>
            <v-btn type="submit" v-else >Save</v-btn>
          </form>
        </v-flex>
      </v-layout>
    </div>
  </v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";
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
      error: "",
      snackbar: false,
      snackbarColor: "error",
      snackText: "Error: please fill all fields correctly"
    };
  },
  computed: {
    ...mapState(["api_state"]),
    isEdit() {
      // if the name is profile Edit, then this is an edit page
      return this.$route.name == "ProfileEdit";
    }
  },
  methods: {
    // map the login action from vuex
    ...mapActions(["registerByUser", "editUser"]),
    register() {
      // store the promise instance
      this.$validator.validateAll().then(result => {
        if (result) {
          let promise;
          if (this.isEdit) {
            // edit mode
            promise = this.editUser({
              id: this.id,
              username: this.username,
              password: this.password,
              password_again: this.passwordAgain,
              location: this.location,
              tel: this.tel
            }).then(res => {
              // go to the detail page
              // redirect request from another view
              this.$router.push({
                name: "ProfileDetail",
                // pass with user's data
                params: { user: res.data }
              });
            });
          } else {
            // register mode
            promise = this.registerByUser({
              username: this.username,
              password: this.password,
              password_again: this.passwordAgain,
              location: this.location,
              tel: this.tel
            }).then(() => {
              // go to main page
              console.log(this);
              if (this.$route.query.redirect) {
                // redirect request from another view
                this.$router.push(this.$route.query.redirect);
              } else {
                // go to previous page, if it's user direct to login
                this.$router.go(-2);
              }
            });
          }
          promise.catch(err => {
            if (err.response.data.username) {
              this.snackText = err.response.data.username[0];
            }
            this.snackbar = true;
            this.snackbarColor = "error";
            this.error = err.response.data;
            this.$store.commit("API_READY");
          });
        }
      });
    }
  },
  mounted() {
    if (this.isEdit) {
      this.$store.dispatch("getUserDetail").then(res => {
        // map these inpo to the input area
        this.username = res.data.username;
        this.location = res.data.location;
        this.tel = res.data.tel;
        this.id = res.data.id;
        // and let this page could be render
        this.$store.commit("API_READY");
      });
    } else {
      // and let this page could be render
      this.$store.commit("API_READY");
    }
  },
  components: {
    addr
  }
};
</script>
