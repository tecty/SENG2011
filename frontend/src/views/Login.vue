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
    login(){
      this.axios.post('api-token-auth/',{
        username: this.username,
        password: this.password,
      })
      .then(res => {
        this.$store.token =  res.data.token;
      })
      .catch(err => {
        this.error = "Wrong Username or Password";
      })
    }
  }

}
</script>
