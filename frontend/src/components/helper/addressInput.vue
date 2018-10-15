<template>
  <places
    v-model="form.country.label"
    placeholder="Where are we going ?"
    @change="val => { form.country.data = val }"
    :options="{ countries: ['AU'] }">
  </places>
</template>


<script>
import Places from 'vue-places';
export default {
  data() {
    return {
      form: {
        country: {
          label: null,
          data: {},
        },
      },
    };
  },
  components: {
    Places
  }
}
</script>
