// router of posts
export default [
  {
    path: "/post/create",
    name: "PostCreate",
    component: () => import("@/views/post/Create.vue")
  },
  {
    path: "/post",
    name: "PostList",
    component: () => import("@/views/post/Show.vue")
  }
];
