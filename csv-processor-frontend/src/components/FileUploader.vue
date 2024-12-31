<template>
    <div>
      <!-- File Selection -->
      <input type="file" @change="handleFileUpload" />
      <button
        v-if="!fileId"
        :disabled="!file"
        @click="uploadFile"
        class="btn"
      >
        Upload
      </button>
  
      <!-- Analyze Button -->
      <button
        v-if="fileId && !processedFilePath"
        @click="analyzeFile"
        class="btn"
      >
        Analyze
      </button>
  
      <!-- Download Button -->
      <button
        v-if="processedFilePath"
        @click="downloadFile"
        class="btn"
      >
        Download Processed File
      </button>
  
      <!-- Display Message -->
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  
  <script>
  import axios from "@/axios"; // Your custom Axios instance with baseURL & CSRF
  
  export default {
    data() {
      return {
        file: null,             // Holds the selected file
        fileId: null,          // Holds the file ID returned from the backend
        processedFilePath: null, // Holds the path of the processed file
        message: "",           // Status messages
      };
    },
    computed: {
      // If you want to rely on a dummy 'authToken' to satisfy your route guard
      // (session auth alone doesn't use a token, but we'll leave this as-is).
      isAuthenticated() {
        return !!localStorage.getItem("authToken");
      },
    },
    methods: {
      // Handle file selection
      handleFileUpload(event) {
        console.log("handleFileUpload");
        this.file = event.target.files[0];
        if (this.file) {
          this.message = `Selected file: ${this.file.name}`;
        }
      },
  
      // Upload file to the backend
      async uploadFile() {
        console.log("uploadFile");
        if (!this.file) {
          this.message = "Please select a file to upload.";
          return;
        }
  
        const formData = new FormData();
        formData.append("file", this.file);
  
        try {
          // Because our axios instance has baseURL: "http://localhost:8000",
          // we can just call "/api/upload/" instead of the full URL
          const response = await axios.post("/api/upload/", formData, {
            headers: {
              // Only needed for file upload; session-based auth doesn't need Authorization
              "Content-Type": "multipart/form-data",
            },
          });
          console.log("Upload Response:", response.data);
          this.message = response.data.message;
          this.fileId = response.data.file_id; // Save the file ID for analysis
        } catch (error) {
          console.error("Upload Error:", error.response);
          this.message = `Error uploading file: ${
            error.response?.data?.error || "Unknown error"
          }`;
        }
      },
      async fetchUserName() {
      try {
        console.log('fetchUserName');
        const response = await axios.get("/api/user-info/");
        this.userName = response.data.username;
        console.log("this.userName: ",this.userName);
      } catch (error) {
        console.error("Error fetching user info:", error);
      }
    },
  
      // Analyze the uploaded file
      async analyzeFile() {
        console.log("analyzeFile");
        await this.fetchUserName();
        if (!this.fileId) {
          this.message = "Please upload a file before analyzing.";
          return;
        }
  
        try {
          const response = await axios.put(
            "/api/upload/",
            { file_id: this.fileId }, // JSON payload
            {
              headers: {
                // Session-based auth doesn’t need an Authorization header
                "Content-Type": "application/json",
              },
            }
          );
          console.log("Analyze Response:", response.data);
          this.message = response.data.message;
          this.processedFilePath = response.data.processed_file_path; // Save processed file path
        } catch (error) {
          console.error("Analyze Error:", error.response);
          this.message = `Error analyzing file: ${
            error.response?.data?.error || "Unknown error"
          }`;
        }
      },
  
      // Download the processed file
      async downloadFile() {
        console.log("downloadFile");
        if (!this.processedFilePath) {
          this.message = "No processed file available for download.";
          return;
        }
  
        try {
          const response = await axios.get("/api/upload/", {
            params: { file_path: this.processedFilePath },
            responseType: "blob",
            // No Authorization header needed for session-based
          });
  
          // Trigger file download
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", "processed_file.csv");
          document.body.appendChild(link);
          link.click();
          link.remove();
  
          this.message = "File downloaded successfully.";
        } catch (error) {
          console.error("Download Error:", error.response);
          this.message = `Error downloading file: ${
            error.response?.data?.error || "Unknown error"
          }`;
        }
      },
  
      // Logout user (clears out localStorage token if you’re using a token approach)
      logout() {
        localStorage.removeItem("authToken", "session");
        localStorage.removeItem("refreshToken");
        this.message = "Logged out successfully.";
        this.$router.push("/login");
      },
    },
  };
  </script>
  
  <style>
  h1 {
    font-family: Arial, sans-serif;
    color: #333;
  }
  
  button {
    margin: 10px 5px;
    padding: 10px 15px;
    font-size: 16px;
    cursor: pointer;
    background-color: #006400; 
  }
  
  button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }

  .btn {
  background-color: #006400;
  color: #fff;
  padding: 8px 12px;
  text-decoration: none;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: inline-block;
  margin: 10px 5px;
  transition: background-color 0.2s ease;
  font-size: 16px;
}
.btn:hover {
  background-color: #008000;
}
.btn:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
  
  </style>
  