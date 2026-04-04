# Finance Data Processing Backend

## Overview
This project is a backend system for managing financial records with role-based access control and dashboard analytics.

## Features
- User management with roles (Admin, Analyst, Viewer)
- Financial records CRUD operations
- Role-based access control
- Dashboard summary API (income, expense, balance)

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

## API Endpoints

### Financial Records
- GET /api/records/
- POST /api/records/

### Dashboard
- GET /api/dashboard/summary/

## Setup Instructions
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   pip install django djangorestframework
4. Run migrations:
   python manage.py migrate
5. Start server:
   python manage.py runserver

## Note
This is a backend API project. There is no homepage UI. Please use the following endpoints to test:

- http://127.0.0.1:8000/api/records/
- http://127.0.0.1:8000/api/dashboard/summary/
- http://127.0.0.1:8000/admin/
