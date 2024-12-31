CSV Processor
A Django + Vue application that processes CSV files. Users can sign up, log in, upload files, analyze them, and download processed results.


Table of Contents
Prerequisites
Project Structure
Setup & Installation
1. Clone the Repository
2. Create and Activate a Python Virtual Environment
3. Install Python Dependencies
4. Set Up the Database (SQLite)
5. Run Django Server
6. Install Node Dependencies
7. Run the Vue Dev Server
Usage
Accessing the Application
Creating an Account
Uploading and Processing CSVs
Environment Variables
Common Issues
Contributing
License
Prerequisites
Python 3.10+ (or your chosen version)
Node.js 16+ (or your chosen version)
npm or yarn (for frontend dependencies)
Git (to clone the repository)
Project Structure
A high-level overview of the important directories/files:

php
Copy code
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
(Adjust this structure if you’re using a different setup.)

Setup & Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name
2. Create and Activate a Python Virtual Environment
It’s recommended to use a virtual environment to keep Python dependencies isolated:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows
3. Install Python Dependencies
bash
Copy code
cd csv_processor  # or wherever your manage.py is located
pip install -r requirements.txt
(If your requirements are listed in requirements.txt. Adjust if needed.)

4. Set Up the Database (SQLite)
By default, Django is configured to use SQLite. Just run migrations:

bash
Copy code
python manage.py migrate
Optional: Create a superuser if you need admin access:

bash
Copy code
python manage.py createsuperuser
5. Run Django Server
Start the Django development server (port 8000 by default):

bash
Copy code
python manage.py runserver
Check that it’s running at http://localhost:8000. You should see “Page not found” or the default Django page if your root URL isn’t defined.

6. Install Node Dependencies
Open a new terminal (still in the repo root or in the frontend folder if that’s how your project is structured):

bash
Copy code
cd ../frontend  # adjust path if your frontend is in a separate folder
npm install
# OR if you use yarn:
# yarn
7. Run the Vue Dev Server
bash
Copy code
npm run dev
# OR
# yarn dev
This will typically start the Vue app on http://localhost:5173 (or another port, depending on your Vite/Webpack config). The Vue application will proxy requests to Django or directly call http://localhost:8000 if that’s how it’s configured.

Usage
Accessing the Application
Django is at http://localhost:8000/.
Vue is at http://localhost:5173/ (or a similar dev server port).
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
CORS/CSRF Errors:

Make sure you have correct CORS_ALLOWED_ORIGINS and CSRF_TRUSTED_ORIGINS in settings.py.
Use withCredentials: true in Axios if you rely on session-based authentication.
Port Conflicts:

If port 8000 or 5173 is already in use, stop the other service or update the port in your vite.config.js or runserver command (python manage.py runserver 8001).
No module named ...:

Ensure your virtual environment is activated and dependencies are installed.
“404 Not Found” for the Vue routes:

Check that your Vue router has the correct path definitions (/login, /signup, /file-upload).
Contributing
Fork the repo
Create a new branch for your feature
Commit your changes
Open a Pull Request
We welcome improvements!

License
This project is licensed under the MIT License. Feel free to modify and distribute.