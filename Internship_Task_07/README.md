# Task 7 – Pytest Unit Testing Suite

## Project Title
**Automated API Testing Using Pytest and FastAPI**

## Abstract
This project focuses on developing an automated testing suite for a FastAPI application using the Pytest framework. A separate in-memory SQLite database is used to test database operations without affecting the main application database.

## Features
- Automated API testing using Pytest.
- Separate in-memory test database.
- Database session dependency override.
- API response and status code validation.
- Student creation and retrieval tests.
- Duplicate email and missing student error testing.
- Invalid input validation.
- Automated database cleanup.

## Technologies Used
- Python 3.11.9
- FastAPI
- SQLAlchemy
- SQLite
- Pytest
- HTTPX
- Pydantic

## How to Run

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the test suite:

```powershell
python -m pytest tests -v
```

## Test Results
**8 test cases passed successfully.**

## Conclusion
The project successfully demonstrates automated API testing using Pytest, separate database instances, and assertion-based validation.