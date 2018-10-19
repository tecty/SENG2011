// router of bids
export default [
  {
    path: "/post/:postId/bid",
    name: "BidCreate",
    component: () => import("@/views/bid/Create.vue")
  }
];
