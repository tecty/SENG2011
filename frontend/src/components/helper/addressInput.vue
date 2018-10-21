<template>
  <places
    v-model="form.country.label"
    :placeholder="hint"
    @change="val => {
      form.country.data = val; 
      $emit('confirmLocation', {
        address: val.value,
        lat: val.latlng.lat,
        lng: val.latlng.lng
      })
    }"
    :options="{ countries: ['AU'] }"
  >
  </places>
</template>



<script>
import Places from "vue-places";
export default {
  props: ["hint", "address"],
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
  },
  mounted() {
    if (this.address) {
      this.form.country.label = this.address;
    }
  }
};
</script>
