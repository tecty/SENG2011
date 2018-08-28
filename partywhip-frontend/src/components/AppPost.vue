<template>
  <v-content>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center fill-height>
        <img src="@/assets/logo.png" alt="Vuetify.js" class="mb-5">
        <blockquote>
          &#8220;This is Post page.&#8221;
        </blockquote>
          {{ posts }}
      </v-layout>
    </v-slide-y-transition>
  </v-container>
    </v-content>
</template>

<script>
import axios from 'axios'
var sessionUrl = 'http://127.0.0.1:8000/api-v0/posts/?format=json'
var uname = 'zhilu'
var pass = '332301'
export default {
  data () {
    return {
      posts: []
    }
  },
  mounted () {
    axios.get(sessionUrl, {}, {
      auth: {
        username: uname,
        password: pass
      }
    }).then(response => {
      // JSON responses are automatically parsed.
      console.log(response)
      this.posts = response.data
    })
    .catch(error => {
      console.log(error)
      console.log(error.response)
    })
  }
}
</script>
