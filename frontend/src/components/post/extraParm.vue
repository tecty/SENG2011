<template>
  <div v-if="criteria.length > 0">
    <h3 class="headline primary--text ">Extra Requirements</h3>
    <div v-for="item in showParms" :key="item.id">
      {{ item.key }}: {{ item.value }}
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  // the data of this post
  props: ["criteria"],
  data() {
    return {};
  },
  computed: {
    ...mapState({
      // map the epList to local naming scheme
      epList: state => state.extraParam.epList
    }),
    showParms() {
      return this.epList.filter(el => this.criteria.includes(el.id));
    }
  },
  mounted() {
    this.$store.dispatch("requireExtraParams");
  }
};
</script>
