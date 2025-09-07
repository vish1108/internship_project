# Internship Project - Task Management API

A simple **Task Management API** built with **Django** and **Django REST Framework**.  
It supports **user registration, login (JWT)**, and **task management** (CRUD tasks).

---

## Features
- User Registration & JWT Login
- View & Update Profile
- Create, Update, Delete, and List Tasks
- Only task owner can manage their tasks
- Fetch tasks completed in the last 7 days
- Swagger & Redoc API documentation

---

## Setup Instructions

1. Clone the repo:
    ```bash
    git https://github.com/vish1108/internship_project
    cd internship_project

2. Create virtual environment:
      ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    # source venv/bin/activate  # Linux/Mac

3. Install dependencies:
   ```bash
    pip install -r requirements.txt

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate


5. Run server:
     ```bash
     python manage.py runserver 8080


  API Endpoints
User

POST /api/users/register/ - Register user

POST /api/users/login/ - JWT Login

GET /api/users/profile/ - View profile

PUT /api/users/profile/ - Update profile

Tasks

GET /api/tasks/ - List tasks

POST /api/tasks/ - Create task

GET /api/tasks/<id>/ - Get task

PUT /api/tasks/<id>/ - Update task

DELETE /api/tasks/<id>/ - Delete task

GET /api/tasks/recent-completed/ - Tasks completed in last 7 days

API Docs

Swagger: /swagger/

Redoc: /redoc/

DRF Docs: /api/tasks/docs/ & /api/users/docs/






