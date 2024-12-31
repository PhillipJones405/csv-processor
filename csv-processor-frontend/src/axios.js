// src/axios.js
import axios from "axios";

// Create an Axios instance with your desired defaults
const axiosInstance = axios.create({
  baseURL: "http://localhost:8000", // or whatever your Django server is
  withCredentials: true,            // ensure cookies are sent in all requests
});

// OPTIONAL: If you want Django-style CSRF automatically attached in every request
axiosInstance.interceptors.request.use((config) => {
  // Grab the csrftoken from the cookie
  const csrfToken = document.cookie
    .split("; ")
    .find((row) => row.startsWith("csrftoken="))
    ?.split("=")[1];

  if (csrfToken) {
    config.headers["X-CSRFToken"] = csrfToken;
  }
  return config;
});

export default axiosInstance;
