<template>
  <div class="post">
    <h1>post</h1>
    <p>
      {{posts}}
    </p>
  </div>
</template>

<script>
export default {
  name:"post",
  data() {
    return {
      posts:[],
    }
  },
  mounted(){
    this.axios
      .get("http://localhost:8000/api-v0/posts/")
      .then(res =>{
        this.posts = res.data;
      })
      .catch(err => {
        console.log(err);
      })
      
  }
}
</script>

<style scoped>

</style>
