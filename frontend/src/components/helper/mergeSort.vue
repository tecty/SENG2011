<template>
  <v-layout mb-1>
    <v-flex>
      <div>
        <v-select
          :items="sortBy"
          label="Sort by"
          @change="selecteSortBy"
        ></v-select>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "sortingSelector",
  props: ["sortBy", "list"],
  data() {
    return {
      selectVal: ""
    };
  },
  methods: {
    matchSortParameter() {
      var compareFunc = (a, b) => {
        return a.id - b.id;
      };
      switch (this.selectVal) {
        case "Sort by offer price":
          compareFunc = (a, b) => {
            return parseInt(a.price, 10) - parseInt(b.price, 10);
          };
          break;
        case "Lastest":
          compareFunc = (a, b) => {
            return a.id - b.id;
          };
          break;
        case "Sort by bidder name":
          compareFunc = (a, b) => {
            return a.owner.username.localeCompare(b.owner.username);
          };
          break;
        case "Sort by issuer name":
          compareFunc = (a, b) => {
            return a.event.owner.username.localeCompare(b.event.owner.username);
          };
          break;
        case "Sort by Budget":
          compareFunc = (a, b) => {
            return parseInt(a.budget, 10) - parseInt(b.budget, 10);
          };
          break;
        case "Sort by Number of bids":
          compareFunc = (a, b) => {
            return a.bid_set.length - b.bid_set.length;
          };
          break;
        case "Sort by Number of people":
          compareFunc = (a, b) => {
            return a.peopleCount - b.peopleCount;
          };
          break;
        case "Sort by Event time":
          compareFunc = (a, b) => {
            let da = new Date(a.event.eventTime);
            let db = new Date(b.event.eventTime);
            return da - db;
          };
          break;
        case "Sort by Bid Ending time":
          compareFunc = (a, b) => {
            let da = new Date(a.event.bidClosingTime);
            let db = new Date(b.event.bidClosingTime);
            return da - db;
          };

          break;

        default:
          this.$emit("sorted", this.list);
          return;
          break;
      }
      let sorted = this.mergeSort(this.list, compareFunc);
      this.$emit("sorted", sorted);
    },
    selecteSortBy(label) {
      console.log(label);
      this.selectVal = label;
      this.matchSortParameter();
    },
    mergeSort(list, compareFunc) {
      var temp = this.mergeSortRecu(list, 0, list.length - 1, compareFunc);
      return temp;
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