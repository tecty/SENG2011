<template>
  <v-select
    v-model="selected"
    :items="sortBy"
    label="Sort by"
    @change="mergeSort"
  ></v-select>
</template>

<script>
export default {
  name: "sortingSelector",
  props: ["value", "sortBy", "list"],
  data() {
    return {
      // default callback is id descding
      selected: { f: (a, b) => a.id - b.id }
    };
  },
  computed: {
    compareFunc() {
      // return the call back provided
      // as an function
      return this.selected.f;
    }
  },
  methods: {
    mergeSort() {
      // console.log(this.compareFunc)
      // call the merge sort
      this.$emit("input", this.mergeSortRecu(
        this.value,
        0,
        this.value.length - 1,
        this.compareFunc
      ));
    },
    mergeSortRecu(list, lo, hi, compareFunc) {
      var newList = list.slice();
      if (lo < hi) {
        var mid = Math.floor((lo + hi) / 2);
        newList = this.mergeSortRecu(list, lo, mid, compareFunc);
        newList = this.mergeSortRecu(newList, mid + 1, hi, compareFunc);
        newList = this.merge(newList, lo, mid, hi, compareFunc);
      }
      return newList;
    },
    merge(newList, lo, mid, hi, compareFunc) {
      var buffer = newList.slice();
      // console.log(buffer);
      var i = lo;
      var j = mid + 1;
      var k = 0;
      while (k < hi - lo + 1) {
        if (i > mid) {
          buffer[lo + k] = newList[j];
          j++;
        } else if (j > hi) {
          buffer[lo + k] = newList[i];
          i++;
        } else if (compareFunc(newList[i], newList[j]) <= 0) {
          //newList[i] sits before newList[j] ==>  compareFunc(newList[i],newList[j]) < 0
          buffer[lo + k] = newList[i];
          i++;
        } else {
          buffer[lo + k] = newList[j];
          j++;
        }
        k++;
      }
      return buffer;
    }
  }
};
</script>
