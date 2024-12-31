import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    // Track whether the user is logged in
    isLoggedIn: false,
    userName: "",
    // Optionally store user info, tokens, etc.
  }),
  actions: {
    setLoggedIn(value) {
      this.isLoggedIn = value;
    },
    setUserName(name) {
        this.userName = name;
      },
  },
});
