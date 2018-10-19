<template>
  <div>
    <h3 class="headline primary--text ">Extra Requirements</h3>
    <div v-for="item in showParms" :key="item">
      {{ item.key }}: {{ item.value }}
    </div>
  </div>
</template>
<script>
export default {
  // the data of this post
  props: ["criteria"],
  data() {
    return {};
  },
  computed: {
    showParms: function() {
      let ret = [];
      this.criteria.forEach(el => {
        ret.push(this.$store.state.extraParameter.find(ep => ep.id == el));
      });
      return ret;
    }
  },
  mounted() {
    this.$store.dispatch("requireExtraParams");
  }
};
</script>
