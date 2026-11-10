
# Task 6 – SQLite Relational Integration

## Project Title
SQLite Relational Integration Using FastAPI and SQLAlchemy

## Abstract
This project demonstrates the integration of a SQLite relational database with a FastAPI application using SQLAlchemy ORM. It allows users to be created, stored, retrieved, and connected with multiple API records. Database sessions are managed through FastAPI dependencies.

## Features
- SQLite database connection
- SQLAlchemy ORM models
- User and API record relationships
- Create and retrieve users
- Create and retrieve user records
- Duplicate email validation
- Error handling for missing users
- Automated testing using Pytest

## Technologies Used
- Python 3.11.9
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn
- Pytest

## How to Run

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start the application:

```powershell
python -m uvicorn app.main:app --reload
```

Open Swagger documentation:

http://127.0.0.1:8000/docs

## Run Tests

```powershell
python -m pytest tests -v
```

## Database Tables
1. Users – Stores user ID, name, and email.
2. API Records – Stores record ID, data, and associated user ID.

## Test Results
All 7 automated tests passed successfully.

## Conclusion
The project successfully integrates a SQLite relational database with a FastAPI application using SQLAlchemy ORM. It demonstrates database connections, relational mappings, session operations, API integration, and automated testing.
