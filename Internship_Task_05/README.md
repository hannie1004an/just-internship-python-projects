
# Task 5 - Pydantic Validation Schemas

## Introduction
This project demonstrates input validation in a REST API using FastAPI and Pydantic. It validates user data and rejects invalid inputs based on predefined constraints.

## Objectives
- Define Pydantic models with type annotations.
- Apply custom field validation constraints.
- Validate incoming POST request data.
- Reject invalid input values.
- Return clear validation error responses.
- Test API functionality using Pytest.

## Technologies and Tools Used
- Python 3.11.9
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX
- Visual Studio Code

## Project Structure

```text
Internship_Task_05/
├── app/
│   └── main.py
├── tests/
│   └── test_api.py
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Welcome message |
| POST | /validate | Validates user input |

## Validation Rules
- Name: Minimum 2 and maximum 50 characters.
- Age: Minimum 18 and maximum 100.
- Email: Must match the specified email pattern.

## Run the Server

```bash
python -m uvicorn app.main:app --reload --port 8001
```

Open API documentation:
http://127.0.0.1:8001/docs

## Run Tests

```bash
python -m pytest tests -v
```

## Result
The Input Validation API System was successfully developed using FastAPI and Pydantic. Valid input was accepted, while invalid age, email, and name values were rejected. All five automated tests passed successfully.
