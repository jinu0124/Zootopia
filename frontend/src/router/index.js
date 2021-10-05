import Vue from "vue";
import VueRouter from "vue-router";
import Stock from "../views/Stock";
import News from "../views/News";
import VueMoment from "vue-moment";
import Home from "../views/Home"

Vue.use(VueMoment);
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    alias: ["/home"],
    name: "Home",
    component: Home,
  },
  {
    path: "/news",
    name: "News",
    component: News,
  },
  {
    path: "/stock",
    name: "Stock",
    component: Stock,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
