import { createRouter, createWebHistory } from "vue-router";
import FileUploader from "../components/FileUploader.vue";
import Login from "../components/Login.vue";
import Signup from "../components/Signup.vue";

const routes = [
  // { path: "/file-upload", component: FileUploader, meta: { requiresAuth: true } },
  { path: "/file-upload", component: FileUploader },
  // { path: "/", component: FileUploader, meta: { requiresAuth: true } },
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem("authToken");
  if (to.meta.requiresAuth && !isAuthenticated) {
    next("/login");
  } else {
    next();
  }
});

export default router;
