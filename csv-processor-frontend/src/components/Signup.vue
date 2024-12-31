<template>
    <div>
      <h2>Signup</h2>
      <form @submit.prevent="signup">
        <div>
          <label>Email</label>
          <input v-model="email" type="email" required />
        </div>
        <div>
          <label>Password</label>
          <input v-model="password" type="password" required />
        </div>
        <button type="submit">Signup</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </template>
<script>
// import axios from "axios";
import axios from "@/axios"; 

export default {
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async signup() {
      try {
        // Fetch the CSRF token from cookies
        console.log('get Token');
        const csrfToken = document.cookie
          .split("; ")
          .find((row) => row.startsWith("csrftoken="))
          ?.split("=")[1];

        if (!csrfToken) {
          throw new Error("CSRF token is missing.");
        }

        console.log("CSRF Token:", csrfToken);

        // Send signup request with CSRF token
        const formData = new FormData();
formData.append("email", this.email);
formData.append("password1", this.password);
formData.append("password2", this.password);

// await axios.post("http://localhost:8000/api/signup/", formData, {
//   headers: { "X-CSRFToken": csrfToken },
//   withCredentials: true,
// });
axios.post("http://localhost:8000/api/signup/", {
  email: this.email,
  password1: this.password,
  password2: this.password,
}, {headers: { "X-CSRFToken": csrfToken }, withCredentials: true })
.then(response => {
  console.log("Signup success:", response.data);
  localStorage.setItem("authToken", "session"); 

  // Now navigate to /upload in Vue
  this.$router.push("/file-upload");
})
.catch(error => {
  console.log("Signup error:", error.response?.data || error);
});
        console.log("Signup Response:", response.data);
        this.error = "Signup successful! Please log in.";
        // Inside your `try` block, after signup success:
this.error = null;
// Just push the user to the /upload route in Vue Router
this.$router.push("/file-upload");
      } catch (error) {
        console.error("Signup Error:", error.response);
        console.error("Signup Error Details:", error.response?.data);
        this.error = error.response?.data?.error || "Signup failed. Please try again.";
      }
    },
  },
};
</script>
