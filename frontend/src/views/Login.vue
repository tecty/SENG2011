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
// import { mapActions } from 'vuex'

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
    // ...mapActions(["loginByCredential"]),
    login(){
      // pass the user login credential 
      this.$store.dispatch("loginByCredential",{
        username: this.username,
        password: this.password,
      })
      .then(() =>{
        // go to the previous page with logined credential 
        this.$router.push('/');
      })
      .catch(err => {
        this.error = err;
        console.log(err);
        // promt the error message to let user try again 
        this.error = "Wrong Username or Password";
      })
    }
    // login(){
    //   this.axios.post('api-token-auth/',{
    //     username: this.username,
    //     password: this.password,
    //   })
    //   .then(res => {
    //     // this.$store.token =  res.data.token;
    //     // checkout to login state
    //     axios.defaults.headers.common['Authorization'] = "JWT "+res.data.token;
    //     this.$router.push('/');
    //   })
    //   .catch(err => {
    //     this.error = "Wrong Username or Password";
    //   })
    // }
  }

}
</script>
