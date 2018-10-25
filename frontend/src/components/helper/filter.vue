<template>
  <v-select
    v-model="selected"
    :items="filterBy"
    label="Filter by"
    @change="doFilter"
  ></v-select>
</template>

<script>
export default {
  props: ["value", "filterBy"],
  data() {
    return {
      // default value is all thing is true
      selected: { f: () => true }
    };
  },
  computed: {
    condition() {
      return this.selected.f;
    }
  },
  methods: {
    doFilter() {
      // filter the passed in array
      this.$emit("input", this.filter(this.value, this.selected));
    },
    /**
     * Filter of an array
     * Verify by Filter.dfy
     */
    filter(list) {
      let ret = [];
      for (var i = 0; i < list.length; i++) {
        if (this.condition(list[i])) {
          ret.push(list[i]);
        }
      }
      return ret;
    }
  },
  mounted() {
    // push an empty condition
    this.$emit(
      "input",
      this.filterBy.unshift({
        text: "Default",
        value: { id: 0, f: () => true }
      })
    );
  }
};
</script>

<style>
</style>
