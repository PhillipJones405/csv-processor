<template>
  <div class="app-container">
    <!-- TOP BRAND ROW -->
    <div class="brand-row">
      <!-- LEFT: Image -->
      <img
        src="@/assets/usda-removebg-preview.png"
        alt="AMS Logo"
        class="brand-logo"
      />

      <!-- MIDDLE: Two lines of text -->
      <div class="agency-text">
        <div>Agricultural Marketing Service</div>
        <div>Livestock and Poultry Program</div>
      </div>

      <!-- RIGHT: CSV Processor -->
      <div class="title-right">
        CSV Processor
      </div>
    </div>

    <!-- NAV BAR ROW -->
    <div class="nav-bar">
      <div class="nav-links">
        <router-link class="btn" v-if="isLoggedIn" to="/file-upload">Home</router-link>
        <router-link class="btn" v-if="!isLoggedIn" to="/login">Login</router-link>
        <router-link class="btn" v-if="!isLoggedIn" to="/signup">Signup</router-link>
      </div>
      <div class="nav-logout">
        <button class="btn" v-if="isLoggedIn" @click="logout">Logout</button>
      </div>
    </div>

    <!-- If the user is logged in, optionally show a welcome -->
    <p v-if="authStore.userName" class="welcome">
      Welcome, {{ authStore.userName }}
    </p>

    <!-- MAIN CONTENT (router-view for the rest of the pages) -->
    <router-view />
  </div>
</template>

<script>
import { computed } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

export default {
  name: "App",
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();

    const isLoggedIn = computed(() => authStore.isLoggedIn);

    function logout() {
      localStorage.removeItem("authToken");
      localStorage.removeItem("refreshToken");
      authStore.setLoggedIn(false);
      authStore.setUserName("");
      router.push("/login");
    }

    return {
      authStore,
      isLoggedIn,
      logout,
    };
  },
};
</script>

<style>
/* BASIC PAGE & TEXT RESET */
html, body {
  margin: 10;
  padding: 10;
  font-family: Arial, sans-serif;
  background-color: #222; /* dark background */
  color: #eee;           /* light text */
}

.app-container {
  /* some overall padding if desired */
}

/* BRAND ROW (logo + agency text + CSV Processor) */
.brand-row {
  display: flex;
  align-items: center;
  background-color: #333;
  padding: 10px;
}

/* LOGO IMAGE ON THE LEFT */
.brand-logo {
  width: 120px;     /* adjust as needed */
  height: auto;
  margin-right: 10px;
}

/* MIDDLE TEXT (Agricultural Marketing Service / Livestock & Poultry) */
.agency-text {
  display: flex;
  flex-direction: column;
  font-size: 22px; 
  line-height: 2.2;
  margin-right: 10px; /* space before CSV Processor text */
}

/* RIGHT SIDE TITLE */
.title-right {
  margin-left: 100px;  /* push CSV Processor to the right */
  font-size: 22px;
  font-weight: bold;
}

/* NAV BAR ROW */
.nav-bar {
  display: flex;
  align-items: center;
  background-color: #444;
  padding: 10px;
  gap: 10px;
}

/* LINKS (LEFT PART OF NAV) */
.nav-links {
  display: flex;
  gap: 10px;
}

/* LOGOUT (PUSH TO RIGHT) */
.nav-logout {
  margin-left: auto;
}

/* REUSABLE .btn STYLE FOR BOTH <router-link> AND <button> */
.btn {
  background-color: #006400; /* dark green */
  color: #fff;
  padding: 8px 12px;
  text-decoration: none; /* remove underline from router-link */
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: inline-block;
  transition: background-color 0.2s ease;
  font-size: 14px;
}

/* HOVER EFFECT */
.btn:hover {
  background-color: #008000; /* lighter green on hover */
}

/* OPTIONAL WELCOME TEXT AFTER NAV BAR */
.welcome {
  margin: 10px;
  font-size: 16px;
}
</style>
