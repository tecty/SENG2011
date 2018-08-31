<template>
  <div class="post">
    <h1>post</h1>
    <!-- <p>
      {{posts}}
    </p> -->
    <div v-for="(item, index) in posts" :key="index">
      {{item.title}}
    </div>



  </div>
</template>

<script>
export default {
  name:"post",
  data() {
    return {
      posts:[],
      error:"",
    }
  },
  mounted(){
    this.axios
      .get("posts/")
      .then(res =>{
        this.posts = res.data;
      })
      .catch(err => {
        this.error = err;
        // console.log(err);
        // Console.log(err);
      })
      
  }
}
</script>

<style scoped>

</style>
