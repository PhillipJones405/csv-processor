import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router"; // Import router configuration
import axiosInstance from "./axios";

const pinia = createPinia();


const app = createApp(App);
app.use(pinia);
app.use(router); // Use Vue Router
app.mount("#app");
