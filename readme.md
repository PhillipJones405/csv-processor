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
