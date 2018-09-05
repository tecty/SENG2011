<template>
  <v-layout mt-3>
    <v-slide-y-transition mode="out-in">
      <v-layout row>
        <v-flex xs12 sm8 offset-sm2>
          <v-card>
            <v-toolbar color="light-blue" dark>
              <v-toolbar-side-icon></v-toolbar-side-icon>

              <v-toolbar-title>Tasks</v-toolbar-title>

              <v-spacer></v-spacer>

              <v-btn icon>
                <v-icon>search</v-icon>
              </v-btn>

              <v-btn icon>
                <v-icon>view_module</v-icon>
              </v-btn>
            </v-toolbar>
            <v-expansion-panel two-line focusable>
              <v-expansion-panel-content v-for="post in posts" :key="post.id" avatar>
                <div slot="header">{{ post.id }}{{ post.msg }}</div>
                <v-card>
                  <v-card-title>
                    <div>
                      <span class="grey--text">{{ post.title }}</span><br>
                      <span>{{ post.location }}</span><br>
                      <span>{{ post.poster.username }}</span><br>
                      <span>{{ post.peopleCount }}</span><br> ...
                    </div>
                  </v-card-title>
                  <v-card-actions>
                    <v-btn flat color="orange" 
                    :to="{ name:'BidCreate', params:{postId: post.id} }" >Bid for it</v-btn>
                  </v-card-actions>
                </v-card>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-card>
        </v-flex>
      </v-layout>
    </v-slide-y-transition>
    <v-btn fixed bottom right fab dark color="red" to="/post/create">
      <v-icon dark>add</v-icon>
    </v-btn>
  </v-layout>

</template>


<script>
import axios from "axios";
var sessionUrl = "http://127.0.0.1:8000/api-v0/posts/";
var uname = "zhilu";
var pass = "123456";
export default {
  data() {
    return {
      posts: []
    };
  },
  mounted() {
    axios
      .get(
        sessionUrl,
        {},
        {
          auth: {
            username: uname,
            password: pass
          }
        }
      )
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(response);
        this.posts = response.data;
      })
      .catch(error => {
        console.log(error);
        console.log(error.response);
      });
  }
};
</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
