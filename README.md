# Inspection Management System

A web-based inspection management system built with Django that allows users to manage and track inspections and their conditions.

## Project Overview

This project was built using:
- Django (Web Framework)
- MySQL (Database)
- Bootstrap 5 (Frontend Styling)

## Project Structure

```
├── config/                 # Project configuration directory
│   ├── settings.py        # Django settings and configurations
│   ├── urls.py           # Main URL routing
│   ├── wsgi.py           # WSGI configuration for deployment
│   └── asgi.py           # ASGI configuration for deployment
│
├── inspections/           # The main application directory
│   ├── models.py         # Database models (Inspection, Condition)
│   ├── views.py          # View functions for handling requests
│   ├── admin.py          # Admin interface configuration
│   └── templates/        # HTML templates
│       ├── base.html     # Base template with common structure
│       ├── login.html    # Login page template for the admin
│       ├── home.html     # Dashboard/home page template
│       └── conditions.html # Conditions page template
│
├── manage.py             # Django's command-line utility
├── requirements.txt      # Project dependencies
└── .env                 # Environment variables (database credentials, etc.)
```


## Python Files Explainationa and how they work in the project

### Config Directory
- `settings.py`: Project settings (database, apps, middleware, static files)
- `urls.py`: URL patterns and routing for the entire project
- `wsgi.py`: Web Server Gateway Interface for deployment
- `asgi.py`: Asynchronous Server Gateway Interface for deployment

### Inspections Directory
- `models.py`: Defines database tables (Inspection and Condition models)
- `views.py`: Contains functions that handle web requests and return responses
- `admin.py`: Configures how models appear in Django admin interface
- `apps.py`: Application configuration and settings
- `tests.py`: Contains test cases for the application

### Root Directory
- `manage.py`: Command-line tool for managing the Django project

## Key Features

1. **User Authentication**
   - Secure login system
   - Session management
   - User-specific access through superuser creation

2. **Inspection Management**
   - View all inspections
   - Track inspection details
   - Manage inspection conditions

3. **Condition Tracking**
   - View conditions per inspection
   - Track condition details

## Database Structure

- **Inspection Table**
  - Stores inspection records
  - Links to conditions

- **Condition Table**
  - Stores condition details
  - References parent inspection

## Setup and Installation project

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Configure database in `.env` file
6. Run migrations: `python manage.py migrate`
7. Create superuser: `python manage.py createsuperuser`
8. Run the server: `python manage.py runserver`

## Environment Variables (.env)

# DATABASE
```
DB_NAME=inspection_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

## Access into the website

run "python3 manage.py runserver" and then click on the link : http://127.0.0.1:8000/