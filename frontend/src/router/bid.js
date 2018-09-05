// router of bids
export default [
  {
    path: "/post/:postId/bid",
    name: "BidCreate",
    component: () => import("@/views/bid/Create.vue")
  },
  {
    path: "/bid",
    name: "BidList",
    component: () => import("@/views/bid/Show.vue")
  }
];
