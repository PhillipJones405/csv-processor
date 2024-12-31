# CSV Processor

A **Django + Vue** application that processes CSV files.  
Users can **sign up**, **log in**, **upload files**, **analyze** them, and **download** processed results.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
  1. [Clone the Repository](#1-clone-the-repository)
  2. [Create and Activate a Python Virtual Environment](#2-create-and-activate-a-python-virtual-environment)
  3. [Install Python Dependencies](#3-install-python-dependencies)
  4. [Set Up the Database (SQLite)](#4-set-up-the-database-sqlite)
  5. [Run Django Server](#5-run-django-server)
  6. [Install Node Dependencies](#6-install-node-dependencies)
  7. [Run the Vue Dev Server](#7-run-the-vue-dev-server)
- [Usage](#usage)
  - [Accessing the Application](#accessing-the-application)
  - [Creating an Account](#creating-an-account)
  - [Uploading and Processing CSVs](#uploading-and-processing-csvs)
- [Environment Variables](#environment-variables)
- [Common Issues](#common-issues)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

- **Python 3.10+** (or your chosen version)
- **Node.js 16+** (or your chosen version)
- **npm** or **yarn** (for frontend dependencies)
- **Git** (to clone the repository)

---

## Project Structure

A high-level overview of the important directories/files:

```bash
csv_processor/
├── csv_processor/          # Django project config folder
│   ├── settings.py         # Django settings
│   ├── urls.py             # Django URL configuration
│   └── wsgi.py             # WSGI entry point
├── api/                    # Django app containing views, models, etc.
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── manage.py               # Django management script

frontend/
├── src/
│   ├── components/
│   ├── router/
│   ├── stores/             # Pinia stores
│   ├── App.vue
│   └── main.js
├── public/                 # Static files for Vue
├── package.json            # Node dependencies
└── vite.config.js          # Vue config (if using Vite)

README.md
```
## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name
```
### 2. Create and Activate a Python Virtual Environment
It’s recommended to use a virtual environment to keep Python dependencies isolated:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux

# OR on Windows:
venv\Scripts\activate

# OR with VS Code GUI, CTRL SHIFT P > Create Env
```
### 3. Install Python Dependencies
```bash
cd csv_processor  # or wherever your manage.py is located
pip install -r requirements.txt
```
### 4. Set Up the Database (SQLite), superuser, and run
By default, Django is configured to use SQLite. Just run migrations:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
### 6. Install Node Dependencies
Open a new terminal (still in the repo root or in the frontend folder if that’s how your project is structured):
```bash
cd ../frontend  # adjust path if your frontend is in a separate folder
npm install

# OR if you use yarn:
# yarn

```
### 7. Run the Vue Dev Server
```bash
npm run dev
# OR
# yarn dev
```

This will typically start the Vue app on http://localhost:5173 (or another port, depending on your Vite/Webpack config). The Vue application will proxy requests to Django or directly call http://localhost:8000 if that’s how it’s configured.
XXX

Usage
Accessing the Application
Django is at http://localhost:8000.
Vue is at http://localhost:5173 (or a similar dev server port).
Creating an Account
Navigate to http://localhost:5173/signup.
Enter your email and desired password, then sign up.
Alternatively, use Django admin (http://localhost:8000/admin) if you created a superuser.
Uploading and Processing CSVs
Once logged in, go to Home (http://localhost:5173/file-upload).
Select a CSV file and click Upload.
Click Analyze to process the file on the server.
Click Download Processed File to retrieve the processed CSV.
Environment Variables
If you need custom environment variables (like SECRET_KEY, DEBUG, or API endpoints), you can:

Create a .env file in the Django folder and reference it in settings.py.
For Vue, create a .env file with e.g. VITE_APP_BASE_URL for the backend.
(Adapt as needed for your own environment strategy.)

Common Issues
CORS/CSRF Errors

Make sure you have correct CORS_ALLOWED_ORIGINS and CSRF_TRUSTED_ORIGINS in settings.py.
Use withCredentials: true in Axios if you rely on session-based authentication.
Port Conflicts

If port 8000 or 5173 is already in use, stop the other service or update the port in your vite.config.js or runserver command (python manage.py runserver 8001).
No module named ...

Ensure your virtual environment is activated and dependencies are installed.
“404 Not Found” for the Vue routes

Check that your Vue router has the correct path definitions (/login, /signup, /file-upload).
Contributing
Fork the repo
Create a new branch for your feature
Commit your changes
Open a Pull Request
We welcome improvements!

License
This project is licensed under the MIT License. Feel free to modify and distribute.
