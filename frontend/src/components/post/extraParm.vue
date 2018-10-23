<template>
  <div v-if="criteria.length > 0">
    <h3 class="headline primary--text ">Extra Requirements</h3>
    <p>
      <span v-for="item in showParms" :key="item.id">
        {{item}}<br>
      </span> 
    </p>
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
      return this.epList.filter(el => this.criteria.includes(el.id))
      .map(el=> `${el.key}: ${el.value}`);
    }
  },
  mounted() {
    this.$store.dispatch("requireExtraParams");
  }
};
</script>
