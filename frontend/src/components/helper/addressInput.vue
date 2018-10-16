<template>
  <places
    v-model="form.country.label"
    placeholder="Where are we going ?"
    @change="val => {
      form.country.data = val; 
      $emit('confirmLocation', {
        address: val.value,
        lat: val.latlng.lat,
        lng: val.latlng.lng
      })
    }"
    :options="{ countries: ['AU'] }">
  </places>
</template>


<script>
import Places from "vue-places";
export default {
  data() {
    return {
      form: {
        country: {
          label: null,
          data: {}
        }
      }
    };
  },
  components: {
    Places
  }
};
</script>