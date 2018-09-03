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
import { mapActions, mapGetters } from 'vuex'

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
      error:"",
    }
  },
  methods:{
    // map the login action from vuex 
    ...mapActions(["loginByCredential"]),
    ...mapGetters(["isApiSuccess"]),
    login(){
      // pass the user login credential 
      this.loginByCredential({
        username: this.username,
        password: this.password,
      }).then( () => {

        console.log(this.isApiSuccess())
      })
      // check the state 
      // .then(val => {
      //   if(val == true ){
      //     // login success
      //     // console.log(this.isApiSuccess());
      //     this.$router.go(-1) || this.$router.go("/");
      //   }
      //   else{
      //     console.log(val);
      //     this.error = "Wrong Password Or username";
      //   }
      // })
    }
  }

}
</script>
