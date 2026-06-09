# ProjectHub

## Overview

ProjectHub is a Django-based project management platform that allows users to create, organise and manage projects in a collaborative environment.

The application includes project tracking, categorisation, messaging, file uploads, analytics dashboards and role-based permissions.

This project was developed as part of the Django Frameworks module assignment.

---

## Features

### User Management

* User registration
* User login/logout
* Profile management
* Password reset functionality
* Role-based permissions (Admin, Manager, User)

### Project Management

* Create projects
* View project details
* Edit projects
* Delete projects (Admin only)
* Project categorisation
* Project status tracking
* Search and filtering

### Messaging System

* Send messages between users
* Inbox functionality
* Sent messages
* Archive messages
* Unread message notifications

### Dashboard

* Project statistics
* Project status overview
* Interactive Chart.js analytics
* Recent projects section

### Document Management

* Upload project documents
* Download project documents
* Associate files with projects

### User Experience

* Bootstrap responsive design
* JavaScript enhancements
* Form validation
* Auto-dismiss notifications
* Custom error pages

---

## Technologies Used

### Backend

* Python 3.12
* Django 6.0.5

### Database

* SQLite (Development)
* PostgreSQL (Production)

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js

### Deployment

* Render
* Gunicorn
* WhiteNoise

---

## Database Models

### Profile

Stores additional user information including roles.

### Category

Used to categorise projects.

### Project

Stores project information including:

* Name
* Description
* Status
* Dates
* Stakeholders

### Message

Stores messages sent between users.

### ProjectDocument

Stores uploaded project files.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/projecthub.git
```

Navigate to the project:

```bash
cd projecthub
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

---

## Testing

The following functionality was tested:

* User registration
* User login/logout
* Profile updates
* Password reset workflow
* Project CRUD operations
* Category assignment
* Search and filtering
* Messaging system
* File uploads
* Dashboard analytics
* User role permissions

All core functionality operated as expected.

---

## Deployment

The application is deployed using Render.

Environment variables:

* SECRET_KEY
* DEBUG
* DATABASE_URL

B

Start Command:

```bash
gunicorn projecthub.wsgi
```

---

## Future Improvements

* Team project assignments
* Email notifications
* Real-time messaging
* Activity logs
* Calendar integration
* Advanced reporting

---

## Author

Graham Kingabor

Django Frameworks Assignment 2026


https://github.com/Ghound03/projecthub.git

https://projecthub-rd0m.onrender.com