// router of events
export default [
  {
    path: "/event/create",
    name: "EventCreate",
    component: () => import("@/views/event/Create.vue")
  },
  {
    path: "/event",
    name: "EventList",
    component: () => import("@/views/event/Show.vue")
  },
  {
    path: "/event/:eventId",
    name: "EventDetail",
    component: () => import("@/views/event/Detail.vue")
  }
];
