# Academic Management System

A modular academic management platform built with Django and PostgreSQL.

## Overview

This project demonstrates structured backend architecture using a multi-app Django setup. It manages students, teachers, courses, subjects, enrollments, materials, and parent relationships.

## Core Modules

- Accounts (Custom User Model)
- Students Management
- Teachers Management
- Subjects & Courses
- Enrollment System
- Academic Materials Handling
- Parent Associations

## Technical Highlights

- Custom User Model
- PostgreSQL Database Integration
- Modular Django App Architecture
- ForeignKey & ManyToMany Relationships
- Role-Based Access Logic
- Server-Side Rendering (Django Templates)
- Media Handling Configuration

## Tech Stack

- Python
- Django
- PostgreSQL
- Django ORM
- HTML Templates

## Setup Instructions

1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Configure `.env`
5. Run migrations
6. Start development server

## Note

Media files and environment variables are excluded from version control.

## 🏗️ Architecture

The system follows a modular Django multi-app architecture:

- Each domain (students, teachers, courses, enrollments, materials) is isolated into dedicated apps.
- Custom User model implemented for role-based authentication.
- PostgreSQL used for relational integrity and scalability.
- Media handling configured separately for production readiness.

## ⚙️ Local Setup

1. Clone the repository
2. Create virtual environment:
   python -m venv myenv
3. Activate environment:
   myenv\Scripts\activate
4. Install dependencies:
   pip install -r requirements.txt
5. Configure .env file
6. Run migrations:
   python manage.py migrate
7. Start server:
   python manage.py runserver

## 📸 Application Preview

### 🔐 Authentication
| Login | Signup |
|-------|--------|
| ![](screenshots/login.png) | ![](screenshots/signup.png) |

---

### 🎓 Student Dashboard
![](screenshots/mycourses.png)

---

### 📂 Materials Access
![](screenshots/material.png)

---

### 👨‍🏫 Teacher Dashboard
![](screenshots/teacher-dashboard.png)

---

### ⬆️ Teacher Upload System
![](screenshots/teaacher-upload.png)

---

### 📋 Enrolled Students
![](screenshots/enrolled-students.png)

