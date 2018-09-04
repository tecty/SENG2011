// router of bids
export default [
  {
    path: "/bid/create",
    name: "BidCreate",
    component: () => import("@/views/bid/Create.vue")
  },
  {
    path: "/bid",
    name: "BidList",
    component: () => import("@/views/bid/Show.vue")
  }
];