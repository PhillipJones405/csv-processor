<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div>
          <label>Email</label>
          <input v-model="email" type="email" required />
        </div>
        <div>
          <label>Password</label>
          <input v-model="password" type="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
      <p v-if="error" style="color: red;">{{ error }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import axios from "@/axios";
  import { useAuthStore } from "@/stores/auth";
  import { useRouter } from "vue-router";
  
  const authStore = useAuthStore();
  const router = useRouter();
  
  const email = ref("");
  const password = ref("");
  const error = ref("");
  
  async function login() {
    try {
      // 1) POST /api/login/ to authenticate
      const response = await axios.post(
        "/api/login/",
        { email: email.value, password: password.value },
        { withCredentials: true } // crucial for session cookies
      );
      console.log("Login success:", response.data);
  
      // 2) Mark user as logged in
      authStore.setLoggedIn(true);
  
      // 3) Immediately fetch user info from /api/user-info/
      //    so we can store the username in Pinia.
      const info = await axios.get("/api/user-info/", { withCredentials: true });
      console.log("User info response:", info.data);
  
      if (info.data.authenticated) {
        authStore.setUserName(info.data.username); // <--- CRITICAL
        console.log('in if');
      } else {
        console.log('in else');
        authStore.setUserName("");
      }
      console.log("info.data.username: ", info.data.username);
      console.log("authStore.userName: ", authStore.userName);
      console.log("info: ", info);

  
      // 4) (Optional) If your router guard checks localStorage
      localStorage.setItem("authToken", "session");
  
      // 5) Navigate to a protected route
      router.push("/file-upload");
    } catch (err) {
      console.error("Login error:", err.response?.data || err);
      error.value = err.response?.data?.error || "Login failed.";
    }
  }
  </script>
  