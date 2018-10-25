export default [
  {
    path: "/profile",
    name: "PostDetail",
    component: () => import("@/views/profile/Detail.vue"),
    props: { default: true }
  },
  {
    path: "/profile/edit",
    name: "ProfileEdit",
    component: () => import("@/views/profile/Edit.vue"),
    param: { id:true }
  }
];
