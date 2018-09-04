<template>
  <div>
    <v-form v-model="valid">
      <v-text-field
        v-model="price"
        label="Price"
        required
      ></v-text-field>
    </v-form>
  </div>
</template>

<script>
export default {
  data(){
    return {
      // require a valid function. 
      // here just for silence the error
      valid:"",
      price :"", 
    }
  },
  methods:{

  }
};
</script>
