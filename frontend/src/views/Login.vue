<template>
  <v-form v-model="valid" @submit.prevent="login">
    <v-text-field
      v-model="username" label="Username" required autofocus
    />
    <v-text-field 
      v-model="password" :type="show? 'text':'password'" label="Password" 
      :append-icon= "show ? 'visibility' : 'visibility_off'"
      @click:append="show = !show"
      required 
    />
    <p>{{error}}</p>
    <v-btn @click="login" >Login</v-btn>
  </v-form>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data(){
    return{
      // prevent error because vuetify require this 
      valid: false,
      // input of username and password 
      username:"",
      password:"",
      // if show == true, show the password 
      show:false,
      error:""
    }
  },
  methods:{
    // map the login action from vuex 
    ...mapActions(["loginByCredential"]),
    login(){
      // pass the user login credential 
      this.loginByCredential({
        username: this.username,
        password: this.password,
      })
      .then(() => {
        this.$router.go(-1);
      })
      .catch(() => {
        this.error = "Wrong username or password."  
      })
    }
  },
  

}
</script>
